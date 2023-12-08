import heapq
import plotly.graph_objects as go
import networkx as nx
import numpy as np


def create_graph_with_probabilities(edges):
    graph = {}
    for edge in edges:
        a, b, weight, probability = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append((b, weight, probability))
        graph[b].append((a, weight, probability))
    return graph


def prim_with_probabilities(graph, start):
    mst = []
    visited = set()
    edges = [(0, 0, start, None)]

    while edges:
        total_distance, neg_probability, node, prev = heapq.heappop(edges)
        if node not in visited:
            visited.add(node)
            mst.append((prev, node, -neg_probability, total_distance))
            for next_node, dist, prob in graph[node]:
                if next_node not in visited:
                    heapq.heappush(edges, (total_distance + dist,
                                   neg_probability - prob, next_node, node))
    return mst[1:]  # Exclude the first edge as it is (None, start, 0)


def create_and_draw_mst_with_plotly(mst, start_room):
    G = nx.Graph()
    for edge in mst:
        parent, child, _, weight = edge
        G.add_edge(parent, child, weight=weight)

    # Use the Kamada-Kawai layout as a base
    pos = nx.kamada_kawai_layout(
        G, dist=None, weight='weight', scale=1, center=None, dim=2)

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='grey'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=[node for node in G.nodes()],
        textposition="top center",
        marker=dict(
            showscale=False,
            colorscale='Viridis',
            size=10,
            color='blue',
            line=dict(width=2))
    )

    # Define the figure
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False,
                                   showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False,
                                   showticklabels=False),
                        autosize=False,
                        width=2000,
                        height=950
    ))

    # Add weight labels as annotations
    for edge in G.edges(data=True):
        char1, char2 = edge[:2]
        weight = edge[2]['weight']
        x0, y0 = pos[char1]
        x1, y1 = pos[char2]
        # Position of the weight label is the midpoint of the edge
        fig.add_annotation(
            x=(x0+x1)/2,
            y=(y0+y1)/2,
            xref="x",
            yref="y",
            text=str(weight),
            showarrow=False,
            font=dict(size=10)
        )

    fig.update_layout(title_text="Hospital Layout MST", title_x=0.5)
    fig.show()


edges = [

    # Connections from Outside
    ('Outside', 'Main Entry', 1, 0.3),
    ('Outside', 'Kitchen', 1, 0.3),
    ('Outside', 'Mechanical', 1, 0.3),
    ('Outside', 'Materials', 1, 0.3),
    ('Outside', 'Service Corridor', 1, 0.3),
    ('Outside', 'Left Covered Area Entry', 1, 0.3),
    ('Outside', 'Right Covered Area Entry', 1, 0.3),

    # Connections from Left Covered Area Entry
    ('Left Covered Area Entry', 'Left elevator Corridor', 1., 0.3),

    # Connections from Right Covered Area Entry
    ('Right Covered Area Entry', 'Emergency Service', 1, 0.3),

    # Connections from Service Corridor
    ('Service Corridor', 'CSS', 1.5, 0.5),
    ('Service Corridor', 'Surgery Toilet', 1, 0.6),
    ('Service Corridor', 'Radiology', 1.5, 0.7),
    ('Service Corridor', 'Clinic', 1, 0.8),
    ('Service Corridor', 'Emergency Service', 1.5, 1),
    ('Service Corridor', 'Decont', 1, 0.5),
    ('Service Corridor', 'Left elevator Corridor', 2, 0.1),

    # Connections from the Main Entry
    ('Main Entry', 'Reception', 2, 0.6),

    # Connections from Reception
    ('Reception', 'Waiting Area', 2, 0.7),
    ('Reception', 'Left Covered Area Entry', 3, 0.2),
    ('Reception', 'Reception Toilet', 1, 0.3),
    ('Reception', 'Dining', 2, 1),

    # Waiting Area Connections
    ('Waiting Area', 'Radiology', 1, 0.4),
    ('Waiting Area', 'Sub Waiting Area Clinic', 1, 0.9),
    ('Waiting Area', 'Administration', 2, 0.9),
    ('Waiting Area', 'Lab', 1, 0.7),
    ('Waiting Area', 'Rehab', 1.5, 0.9),
    ('Waiting Area', 'Right Covered Area Entry', 2, 0.1),

    # Administration Connections
    ('Administration', 'Administrator office', 1, 0.9),
    ('Administration', 'H.R.', 1, 0.5),
    ('Administration', 'CONF.', 1, 0.5),
    ('Administration', 'Med Lib', 1.5, 0.5),
    ('Administration', 'Information Service', 1, 0.7),
    ('Administration', 'Med Rec', 1, 0.5),
    ('Administration', 'Business office', 1.5, 0.3),
    ('Administration', 'Registration Admit Discharge', 3, 0.3),

    # Registration Admit Discharge Connections
    ('Registration Admit Discharge', 'Waiting Area', 2, 0.7),
    ('Registration Admit Discharge', 'Data Process', 1, 0.4),

    # Sub Waiting Area Connections
    ('Sub Waiting Area', 'Nurse Station', 1, 1),
    ('Sub Waiting Area', 'Triage', 1.5, 0.9),
    ('Sub Waiting Area', 'Clinic Exam', 2, 0.5),
    ('Sub Waiting Area', 'Nurse Clean RM', 3, 0.3),
    ('Sub Waiting Area', 'Clinic SOL', 3, 0.3),
    ('Sub Waiting Area', 'Clinic Office', 4, 0.4),
    ('Sub Waiting Area', 'Emergency Service', 4, 0.5),
    ('Sub Waiting Area', 'Clinic', 1.5, 0.5),


    # Clinic Area Connections
    ('Clinic', 'Clinic Office', 1.5, 0.5),
    ('Clinic', 'Clinic Exam', 1, 0.3),
    ('Clinic', 'Clinic SOL', 1, 0.3),
    ('Clinic', 'Clinic Clean', 1.5, 0.3),
    ('Clinic', 'Radiology', 1, 0.8),
    ('Clinic', 'Emergency Service', 3, 0.5),

    # Emergency Service Connections
    ('Emergency Service', 'ER Exam', 1, 0.9),
    ('Emergency Service', 'Emergency Service office', 3, 0.3),
    ('Emergency Service', 'ER SOL', 2.5, 0.2),
    ('Emergency Service', 'Isolation', 2, 0.8),
    ('Emergency Service', 'Decont', 4, 0.5),
    ('Emergency Service', 'ER Clean RM', 2, 0.3),
    ('Emergency Service', 'Triage', 1, 0.1),
    ('Emergency Service', 'Waiting', 1, 0.5),

    # Radiology Connections
    ('Radiology', 'Surgery', 5, 0.8),
    ('Radiology', 'Files', 1, 0.3),
    ('Radiology', 'Surgery Office', 1, 0.2),
    ('Radiology', 'Radiology Exam', 1.5, 0.3),
    ('Radiology', 'Ultrasound', 1, 0.9),
    ('Radiology', 'Radiology Clean RM', 2, 0.2),
    ('Radiology', 'Radiology SOL', 2, 0.2),
    ('Radiology', 'ELEC', 3, 0.2),
    ('Radiology', 'RF', 3, 0.9),
    ('Radiology', 'CT', 3, 0.9),
    ('Radiology', 'Control', 3, 0.8),
    ('Radiology', 'Read', 1.5, 0.5),
    ('Radiology', 'DK RM', 1, 0.5),
    ('Radiology', 'Quiet RM', 2, 1),

    # Surgery Connections
    ('Surgery', 'Surgery Clean RM', 1, 0.3),
    ('Surgery', 'Surgery Office', 1, 0.2),
    ('Surgery', 'PACU', 2, 0.7),
    ('Surgery', 'Isolation', 3, 0.8),
    ('Surgery', 'O.R.', 2, 0.9),
    ('Surgery', 'Sub Ster', 2, 0.1),
    ('Surgery', 'Lounge', 3, 1),
    ('Lounge', 'Surgery Toilet', 1, 0.5),
    ('O.R.', 'Sub Ster', 0.5, 0.2),

    # CSS Connections
    ('CSS', 'Surgery', 3, 0.9),
    ('CSS', 'Lounge', 1, 1),

    # Connections from Materials
    ('Materials', 'Left elevator Corridor', 1, 0.5),

]


# Assuming the first room in the first edge is the start room (door)
start_room = edges[0][0]
graph = create_graph_with_probabilities(edges)
mst = prim_with_probabilities(graph, start_room)
create_and_draw_mst_with_plotly(mst, start_room)
