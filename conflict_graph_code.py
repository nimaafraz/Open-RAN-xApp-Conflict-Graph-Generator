
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Define the data for the xApps and their ICPs
xapp_data = {
    'Name': ['MLB', 'CCO', 'ES', 'MRO'],
    'ICPs': [
        ['TTT', 'CIO', 'TXP', 'RET'],
        ['TXP', 'RET'],
        ['TXP'],
        ['TXP', 'TTT', 'CIO', 'NL', 'HYS']
    ]
}

# Convert the data into a DataFrame
xapp_df = pd.DataFrame(xapp_data)

# Initialize a graph
G_with_icps = nx.Graph()

# Add nodes to the graph for each xApp
for xapp in xapp_df['Name']:
    G_with_icps.add_node(xapp)

# This dictionary will hold edges as keys and ICPs as values
edge_labels = {}

# Add edges to the graph if two xApps share a common ICP
# Also, prepare the labels for the edges with the names of the conflicting ICPs
for i, xapp1 in xapp_df.iterrows():
    for j, xapp2 in xapp_df.iterrows():
        if i < j:  # To avoid comparing the same pair twice or comparing an xApp with itself
            # Find the intersection of ICPs between two xApps
            common_icps = set(xapp1['ICPs']).intersection(set(xapp2['ICPs']))
            # If there is any common ICP, it means there's a potential conflict
            if common_icps:
                G_with_icps.add_edge(xapp1['Name'], xapp2['Name'])
                edge_labels[(xapp1['Name'], xapp2['Name'])] = ', '.join(common_icps)

# Draw the graph
plt.figure(figsize=(12, 9))
pos = nx.spring_layout(G_with_icps)  # Positions for all nodes
nx.draw(G_with_icps, pos, with_labels=True, node_size=3500, node_color='skyblue', font_size=20, font_weight='bold')

# Draw edge labels
nx.draw_networkx_edge_labels(G_with_icps, pos, edge_labels=edge_labels, font_color='red')

plt.title('Conflict Graph with ICPs for xApps in Open-RAN Network')
plt.show()
