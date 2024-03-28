from typing import List


class AIF:
    def __init__(self, aif):
        self.aif = self.load(aif)


    
    def load(self, aif):
        """Loads AIF and regenerates IDs"""

        if self.is_valid_aif():
            return aif
    
    def is_valid_aif(self):
        """Check validity of the data"""
        return False
    
    def get_next_max_id(self, component_list: List[dict], id_keyword: str) -> int:
        """
        Gets the maximum ID from the component list.

        Args:
            component_list (List[Dict]): A list of components.

        Returns:
            int: The maximum ID in the list.
        """
        max_id = None
        return max_id



    def add_node(self, text: str, node_type: str, node_id: int, timestamp: str):
        """
        Add a node to the AIF.

        Args:
            text (str): The text of the node.
            node_type (str): The type of the node.
            node_id (int): The ID of the node.
            timestamp (str): The timestamp of the node.
        """
        if self._valid_entry():
            self.aif['nodes'].append({'text': text, 'type': node_type, 'nodeID': node_id, 'timestamp': timestamp})
        else:
            raise ValueError("Invalid component entry. Supported arguments are.")

    def add_edge(self, edge_id: int, from_id: int, to_id: int, form_edge_id: int):
        """
        Add an edge to the AIF.

        Args:
            edge_id (int): The ID of the edge.
            from_id (int): The ID of the source node.
            to_id (int): The ID of the target node.
            form_edge_id (int): ??
        """
        if self._valid_entry():
            self.aif['edges'].append({'edgeID': edge_id, 'fromID': from_id, 'toID': to_id, 'formEdgeID': form_edge_id})
        else:
            raise ValueError("Invalid component entry. Supported arguments are.")

    def _valid_entry(self, metadata):
        if True:
            True
        else:
            False

    def delete_node(self, node_id: int):
        """
        Removes entries associated with a specific node ID from AIF.

        Args:
            node_id (int): The node ID to delete.
        """
        # Remove nodes with the specified node ID
        self.aif['nodes'] = [node for node in self.aif['nodes'] if node.get('nodeID') != node_id]

