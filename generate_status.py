import os
import json

def count_problems(base_path="problem_solving"):
    """Compte les fichiers de solutions par catégorie."""
    stats = {}

    for root, dirs, files in os.walk(base_path):
        category = os.path.basename(root)  # Nom du dossier (catégorie)
        if not files:
            continue  # Ignorer les dossiers sans fichiers
        if category not in stats:
            stats[category] = 0
        stats[category] += len(files)  # Nombre de fichiers dans la catégorie

    return stats

def export_to_markdown(stats, output_path="stats.md"):
    """Export les statistiques au format Markdown."""
    with open(output_path, "w") as f:
        f.write("# Statistiques des Problèmes Résolus\n\n")
        f.write("| Catégorie               | Nombre de Problèmes |\n")
        f.write("|-------------------------|---------------------|\n")
        for category, count in stats.items():
            f.write(f"| {category:<24} | {count:<19} |\n")
        print(f"Statistiques exportées dans {output_path}")

def export_to_json(stats, output_path="stats.json"):
    """Export les statistiques au format JSON."""
    with open(output_path, "w") as f:
        json.dump(stats, f, indent=4)
        print(f"Statistiques exportées dans {output_path}")

if _name_ == "_main_":
    # Compter les problèmes
    stats = count_problems()

    # Afficher les statistiques dans la console
    print("Statistiques des Problèmes Résolus :")
    for category, count in stats.items():
        print(f"- {category}: {count} problèmes")

    # Exporter vers Markdown et JSON
    export_to_markdown(stats)
    export_to_json(stats)
