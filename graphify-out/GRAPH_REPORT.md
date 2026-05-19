# Graph Report - c:\Users\Apu Ghanti\Desktop\docker  (2026-05-19)

## Corpus Check
- Corpus is ~1,025 words - fits in a single context window. You may not need a graph.

## Summary
- 30 nodes · 27 edges · 7 communities (3 shown, 4 thin omitted)
- Extraction: 74% EXTRACTED · 26% INFERRED · 0% AMBIGUOUS · INFERRED: 7 edges (avg confidence: 0.5)
- Token cost: 12,000 input · 4,000 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Flask Web Applications|Flask Web Applications]]
- [[_COMMUNITY_Project Documentation & Rules|Project Documentation & Rules]]
- [[_COMMUNITY_Standalone Flask Application|Standalone Flask Application]]
- [[_COMMUNITY_Docker Compose Stack|Docker Compose Stack]]
- [[_COMMUNITY_Basic Container Print|Basic Container Print]]
- [[_COMMUNITY_Docker App Database|Docker App Database]]
- [[_COMMUNITY_Volume Database Setup|Volume Database Setup]]

## God Nodes (most connected - your core abstractions)
1. `mysql_container Service` - 5 edges
2. `insert_data()` - 3 edges
3. `hello_world()` - 2 edges
4. `insert_data() (compose)` - 2 edges
5. `init.sql (docker_compose)` - 2 edges
6. `graphify.md (Rules)` - 2 edges
7. `flask_container Service` - 2 edges
8. `Print Statement` - 1 edges
9. `init.sql (docker_app)` - 1 edges
10. `users Table` - 1 edges

## Surprising Connections (you probably didn't know these)
- `mysql_container Service` --references--> `init.sql (docker_compose)`  [EXTRACTED]
  projects/docker_compose/Docker-compose.yml → projects/docker_compose/my_sql/init.sql
- `graphify.md (Workflows)` --references--> `graphify.md (Rules)`  [INFERRED]
  .agents/workflows/graphify.md → .agents/rules/graphify.md
- `insert_data() (compose)` --calls--> `mysql_container Service`  [INFERRED]
  projects/docker_compose/flask/app.py → projects/docker_compose/Docker-compose.yml
- `insert_data()` --calls--> `mysql_container Service`  [INFERRED]
  docker_compose/flask/app.py → projects/docker_compose/Docker-compose.yml

## Communities (7 total, 4 thin omitted)

### Community 0 - "Flask Web Applications"
Cohesion: 0.29
Nodes (6): requirements.txt (docker_app), requirements.txt (docker_compose), hello_world(), hello_world() (compose), insert_data(), insert_data() (compose)

### Community 1 - "Project Documentation & Rules"
Cohesion: 0.33
Nodes (5): Docker Build & Run Commands, Docker Compose Commands, Docker Volumes Explanation, graphify.md (Rules), graphify.md (Workflows)

### Community 3 - "Docker Compose Stack"
Cohesion: 0.50
Nodes (4): init.sql (docker_compose), flask_container Service, mysql_container Service, users Table (compose)

## Knowledge Gaps
- **14 isolated node(s):** `Print Statement`, `init.sql (docker_app)`, `users Table`, `hello_world() (compose)`, `users Table (compose)` (+9 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `mysql_container Service` connect `Docker Compose Stack` to `Flask Web Applications`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._
- **Why does `insert_data()` connect `Flask Web Applications` to `Docker Compose Stack`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `mysql_container Service` (e.g. with `insert_data()` and `insert_data() (compose)`) actually correct?**
  _`mysql_container Service` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Print Statement`, `init.sql (docker_app)`, `users Table` to the rest of the system?**
  _14 weakly-connected nodes found - possible documentation gaps or missing edges._