import sys, json
from pathlib import Path
from graphify.build import build_from_json
from graphify.cluster import score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate

def main():
    extraction_path = Path('graphify-out/.graphify_extract.json')
    detection_path  = Path('graphify-out/.graphify_detect.json')
    analysis_path   = Path('graphify-out/.graphify_analysis.json')
    
    extraction = json.loads(extraction_path.read_text(encoding="utf-8"))
    detection  = json.loads(detection_path.read_text(encoding="utf-8"))
    analysis   = json.loads(analysis_path.read_text(encoding="utf-8"))

    G = build_from_json(extraction)
    communities = {int(k): v for k, v in analysis['communities'].items()}
    cohesion = {int(k): v for k, v in analysis['cohesion'].items()}
    tokens = {'input': extraction.get('input_tokens', 0), 'output': extraction.get('output_tokens', 0)}

    # Define descriptive community labels
    labels = {
        0: "Flask Web Applications",
        1: "Project Documentation & Rules",
        2: "Standalone Flask Application",
        3: "Docker Compose Stack",
        4: "Basic Container Print",
        5: "Docker App Database",
        6: "Volume Database Setup"
    }

    # Regenerate questions with real community labels
    questions = suggest_questions(G, communities, labels)

    report = generate(G, communities, cohesion, labels, analysis['gods'], analysis['surprises'], detection, tokens, 'c:\\Users\\Apu Ghanti\\Desktop\\docker', suggested_questions=questions)
    Path('graphify-out/GRAPH_REPORT.md').write_text(report, encoding="utf-8")
    
    # Save the labels file
    Path('graphify-out/.graphify_labels.json').write_text(json.dumps({str(k): v for k, v in labels.items()}, ensure_ascii=False), encoding="utf-8")
    print('Report updated with community labels successfully.')

if __name__ == '__main__':
    main()
