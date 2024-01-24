from qiskit import Aer, transpile, assemble, QuantumCircuit
import networkx as nx
from qiskit.visualization import plot_histogram, plot_circuit_layout

def create_quantum_circuit(graph, gate_dict):
    quantum_circuit = QuantumCircuit(max(graph) + 1)

    for edge in graph.edges:
        node, neighbor = edge
        if edge in gate_dict:
            for gate_info in gate_dict[edge]:
                gate_name, *gate_params = gate_info
                gate_method = getattr(quantum_circuit, gate_name, None)

                if gate_method and callable(gate_method):
                    for qubit in [node, neighbor]:
                        try:
                            gate_method(qubit, *gate_params)
                        except Exception as e:
                            print(f"Erreur lors de l'ajout de la porte {gate_name} avec les paramètres {gate_params} et le qubit {qubit}: {e}")
                else:
                    print(f"Méthode de porte {gate_name} non trouvée ou non appelable sur QuantumCircuit.")

    # Transpiler le circuit pour la compatibilité
    transpiled_circuit = transpile(quantum_circuit, optimization_level=3)

    # Compiler le circuit en un objet QuantumCircuit
    compiled_circuit = assemble(transpiled_circuit)

    return compiled_circuit

def analyze_quantum_graph(graph, gate_dict):
    quantum_circuit = create_quantum_circuit(graph, gate_dict)

    # Ajoutez ici le reste du code pour l'analyse du circuit quantique
    # Pour l'instant, la fonction retourne un résultat factice
    results = "Analyse terminée avec succès !"
    return results

# Exemple d'utilisation
graph_example = nx.Graph()
graph_example.add_edges_from([(0, 1), (1, 2), (2, 0)])

gate_dict_qiskit = {
    (0, 1): [('h',)],
    (1, 2): [('x',)],
    (2, 0): [('h',)],
}

quantum_circuit = create_quantum_circuit(graph_example, gate_dict_qiskit)
print(quantum_circuit)

# Exemple de graphe
graph_example = nx.Graph()
graph_example.add_edges_from([(0, 1), (1, 2), (2, 0)])

# Dictionnaire des portes quantiques pour chaque relation du graphe
gate_dict_qiskit = {
    (0, 1): [('h',)],
    (1, 2): [('h',)],
    (2, 0): [('cz',)]
}

# Dictionnaire des relations entre les portes quantiques et les opérations Qiskit
gate_relations = {
    (0, 1): ['h'],
    (1, 2): ['h'],
    (2, 0): ['cz']
}

# Vérifier que chaque relation dans gate_dict_qiskit est présente dans gate_relations
for relation in gate_dict_qiskit:
    gate_operation = gate_dict_qiskit[relation][0][0]
    gate_representation = str(gate_operation)
    
    if relation not in gate_relations:
        print(f"Relation {relation} manquante dans gate_relations.")
    elif not any(gate_representation in str(gate) for gate in gate_relations[relation]):
        print(f"La relation {relation} dans gate_dict_qiskit n'est pas spécifiée correctement dans gate_relations.")
        print(f"Porte attendue : {gate_representation}")
        print(f"Portes disponibles dans gate_relations[{relation}]: {gate_relations[relation]}")
    else:
        print(f"La relation {relation} est correctement spécifiée dans gate_relations.")

# Analyser le graphe quantique avec les portes définies
results = analyze_quantum_graph(graph_example, gate_dict_qiskit)
print(results)
