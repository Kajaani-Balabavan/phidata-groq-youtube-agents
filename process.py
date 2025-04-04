import nbformat

# Load the notebook
with open('AI_Agent.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Iterate over all cells in the notebook
for cell in nb.cells:
    # Check if the cell has widget metadata
    if 'metadata' in cell and 'widgets' in cell.metadata:
        widgets = cell.metadata['widgets']
        
        # Add 'state' to each widget
        for widget in widgets:
            widget.setdefault('state', {})

# Save the fixed notebook
with open('fixed_notebook.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
