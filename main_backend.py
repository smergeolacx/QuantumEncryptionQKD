import numpy as np
import cirq

def make_DPS(num_qubits, alice_basis, measurement_basis, alice_state):
    qubits = cirq.LineQubit.range(num_qubits)
    circuit = cirq.Circuit()

    for i, qubit in enumerate(qubits):
        if alice_state[i] == 1:
            circuit.append(cirq.X(qubit))

        if alice_basis[i] == 1:
            circuit.append(cirq.H(qubit))

    for i, qubit in enumerate(qubits):
        if measurement_basis[i] == 1:
            circuit.append(cirq.H(qubit))
        circuit.append(cirq.measure(qubit, key=str(qubit)))

    return circuit

def make_COW(num_qubits, alice_basis, bob_basis, alice_state):

    qubits = cirq.LineQubit.range(num_qubits)

    circuit = cirq.Circuit()

    for i in range(num_qubits):
        if alice_state[i] == 1:
            circuit.append(cirq.X(qubits[i]))

    for i in range(num_qubits):
        if alice_basis[i] == 1:
            circuit.append(cirq.H(qubits[i]))

    for i in range(num_qubits):
        phase = np.random.uniform(0, 2 * np.pi)
        circuit.append(cirq.Z(qubits[i]) ** (phase / np.pi))

    for i in range(num_qubits):
        if bob_basis[i] == 1:
            circuit.append(cirq.H(qubits[i]))
        circuit.append(cirq.measure(qubits[i], key=str(qubits[i])))


    return circuit


def main(alice_basis, alice_state, bob_basis, num_qubits = 8, eve = 0, repetitions = 100, protocol = 1):
    last_rep_list = []
    if protocol == 1:
        Protocol = make_COW
    elif protocol == 2:
        Protocol = make_DPS
    qubits = cirq.LineQubit.range(num_qubits)
    if eve == 0:
        print("without eve")
        
        #alice_basis = [np.random.randint(0, 2) for _ in range(num_qubits)]
        #alice_state = [np.random.randint(0, 2) for _ in range(num_qubits)]
        #bob_basis = [np.random.randint(0, 2) for _ in range(num_qubits)]


        expected_key = bitstring(
            [alice_state[i] for i in range(num_qubits) if alice_basis[i] == bob_basis[i]]
        )
        matchkey = 0
        mismatchkey = 0
        circuit = Protocol(num_qubits, alice_basis, bob_basis, alice_state)

        
        result = cirq.Simulator().run(program=circuit, repetitions=repetitions)
        for i in range(repetitions):
            result_bitstring = bitstring([result.measurements[str(q)][i] for q in qubits])
            obtained_key = ''.join(
                [result_bitstring[j] for j in range(num_qubits) if alice_basis[j] == bob_basis[j]]
            )

            if obtained_key == expected_key:
                matchkey += 1
            else:
                mismatchkey += 1

            if i>repetitions-6 or repetitions<=5:
                pass
                
                print()
        print(f"Match count: {matchkey}")
        print(f"Mismatch count: {mismatchkey}")

        # plt.bar(['Match', 'Mismatch'], [matchkey, mismatchkey])
        # plt.xlabel('Outcome')
        # plt.ylabel('Count')
        # plt.title('Key Match/Mismatch Count (Without Eve)')
        # plt.savefig('plot.png')

        
        last_rep_list.append(str(circuit))

        
        l = print_results(alice_basis, bob_basis, alice_state, expected_key, obtained_key)
        return [last_rep_list, str(matchkey), str(mismatchkey), l]
    
    else:

        # With Eve
        print('With Eve')
        #np.random.seed(200)

        #alice_basis = [np.random.randint(0, 2) for _ in range(num_qubits)]
        #alice_state = [np.random.randint(0, 2) for _ in range(num_qubits)]
        #bob_basis = [np.random.randint(0, 2) for _ in range(num_qubits)]
        eve_basis = [np.random.randint(0, 2) for _ in range(num_qubits)]

        expected_key = bitstring(
            [alice_state[i] for i in range(num_qubits) if alice_basis[i] == bob_basis[i]]
        )


        alice_eve_circuit = Protocol(num_qubits, alice_basis, eve_basis, alice_state)
        result = cirq.Simulator().run(program=alice_eve_circuit, repetitions=repetitions)
        #eve_state = [result.measurements[str(q)].item() for q in qubits]
        eve_state = bitstring([result.measurements[str(q)][0] for q in qubits])

        eve_bob_circuit = Protocol(num_qubits, eve_basis, bob_basis, eve_state)
        result = cirq.Simulator().run(program=eve_bob_circuit, repetitions=repetitions)

        #result_bitstring = bitstring([result.measurements[str(q)][0] for q in qubits])
        matchkey = 0
        mismatchkey = 0

        for i in range(repetitions):
            result_bitstring = bitstring([result.measurements[str(q)][i] for q in qubits])
            obtained_key = ''.join(
            [result_bitstring[j] for j in range(num_qubits) if alice_basis[j] == bob_basis[j]]
            )

            if obtained_key == expected_key:
                matchkey += 1
            else:
                mismatchkey += 1

            if i > repetitions - 6 or repetitions <= 5:
                pass

        print(f"Match count: {matchkey}")
        print(f"Mismatch count: {mismatchkey}")

        obtained_key = ''.join(
            [result_bitstring[i] for i in range(num_qubits) if alice_basis[i] == bob_basis[i]]
        )
        tempL = [str(alice_eve_circuit),str(eve_bob_circuit)]
        last_rep_list.append(tempL)
                

        assert expected_key != obtained_key, "Keys shouldn't match"

        l = print_results(alice_basis, bob_basis, alice_state, expected_key, obtained_key)
        return [[str(alice_eve_circuit),str(eve_bob_circuit)], matchkey, mismatchkey, l]
    return obtained_key

def bitstring(bits):
    return ''.join(str(int(b)) for b in bits)

def print_results(alice_basis, bob_basis, alice_state, expected_key, obtained_key):
    l = []
    num_qubits = len(alice_basis)
    basis_match = ''.join(
        ['X' if alice_basis[i] == bob_basis[i] else '_' for i in range(num_qubits)]
    )
    alice_basis_str = "".join(['C' if alice_basis[i] == 0 else "H" for i in range(num_qubits)])
    bob_basis_str = "".join(['C' if bob_basis[i] == 0 else "H" for i in range(num_qubits)])

    l.append(f'{alice_basis_str}')
    l.append(f'{bob_basis_str}')
    l.append(f'{bitstring(alice_state)}') #Alice\'s bits:\t
    l.append(f'{basis_match}') #Bases match::\t
    l.append(f'{expected_key}') #Expected key:\t
    l.append(f'{obtained_key}') #Actual key:\t
    return l


if __name__ == "__main__":
    main()
