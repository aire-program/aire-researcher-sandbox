# Sandbox Resource IDs

The sandbox now auto-derives `resource_id` values directly from notebook filenames. This removes the need to hand-edit IDs when adding or renaming notebooks.

Examples:
- `prompt-design-lab.ipynb` → `notebook:prompt-design-lab`
- `embeddings-semantic-search.ipynb` → `notebook:embeddings-semantic-search`

No manual editing is required—use the filename and the sandbox will generate the matching `resource_id`.
