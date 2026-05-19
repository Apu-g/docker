import sys, json
from pathlib import Path
from graphify.build import build_from_json
from graphify.export import to_html

def main():
    extraction_path = Path('graphify-out/.graphify_extract.json')
    analysis_path   = Path('graphify-out/.graphify_analysis.json')
    labels_raw_path = Path('graphify-out/.graphify_labels.json')
    
    extraction = json.loads(extraction_path.read_text(encoding="utf-8"))
    analysis   = json.loads(analysis_path.read_text(encoding="utf-8"))
    labels_raw = json.loads(labels_raw_path.read_text(encoding="utf-8")) if labels_raw_path.exists() else {}

    G = build_from_json(extraction)
    communities = {int(k): v for k, v in analysis['communities'].items()}
    labels = {int(k): v for k, v in labels_raw.items()}

    if G.number_of_nodes() > 5000:
        print(f'Graph has {G.number_of_nodes()} nodes - too large for HTML viz. Use Obsidian vault instead.')
    else:
        to_html(G, communities, 'graphify-out/graph.html', community_labels=labels or None)
        print('graph.html written - open in any browser, no server needed')

if __name__ == '__main__':
    main()
