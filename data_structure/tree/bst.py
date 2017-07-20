from binary_tree import *


class BinarySearchTree(BinaryTree):
    def insert(self, data):
        new_node = self.make_node()
        self.set_node_data(new_node, data)

        cur = self.get_root()
        # 루트 노드가 없을 때
        if not cur:
            self.set_root(new_node)
            return
        # 삽입할 노드의 위치를 찾아 삽입
        while True:
            # 삽입할 데이터가 현재 노드 데이터보다 작을 때
            if data < self.cur.get_data():
                # 왼쪽 자식 노드 존재하면
                if self.get_left_sub_tree(cur):
                    cur = self.get_left_sub_tree(cur)
                # 존재하지 않으면 노드 삽입
                else:
                    self.make_left_sub_tree(cur, new_node)
                    break
            else:
                if self.get_right_sub_tree(cur):
                    cur = self.get_right_sub_tree(cur)
                else:
                    self.make_right_sub_tree(cur, new_node)
                    break

    def search(self, target):
        cur = self.get_root()

        while cur != None:
            if target == self.get_node_data(cur):
                return cur
            elif target < self.get_node_data(cur):
                cur = self.get_left_sub_tree(cur)
            else:
                cur = self.get_right_sub_tree(cur)

        return cur

    def remove_left_sub_tree(self, cur):
        del_node = self.get_left_sub_tree(cur)
        self.make_left_sub_tree(cur, None)
        return del_node

    def remove_right_sub_tree(self, cur):
        del_node = self.get_right_sub_tree(cur)
        self.make_right_sub_tree(cur, None)
        return del_node

    def remove_leaf(self, parent, del_node):
        # 루트 노드 지울 때
        if del_node == self.get_root():
            self.set_root(None)
            return del_node

        if self.get_left_sub_tree(parent) is del_node:
            self.remove_left_sub_tree(parent)
        else:
            self.remove_right_sub_tree(parent)
        return del_node

    def remove_one_child(self, parent, del_node):
        pass

    def remove_two_children(self, del_node):
        pass

    def remove(self, target):
        del_parent = self.get_root()
        del_node = self.get_root()

        while True:
            if del_node == None:
                return None

            if target == self.get_node_data(del_node):
                break
            elif target < self.get_node_data(del_node):
                del_parent = del_node
                del_node = self.get_left_sub_tree(del_node)
            else:
                del_parent = del_node
                del_node = self.get_right_sub_tree(del_node)

            if self.get_left_sub_tree(del_node) is None and \
                            self.get_right_sub_tree(del_node) is None:
                return self.remove_leaf(del_parent, del_node)

            elif self.get_left_sub_tree(del_node) is None or \
                            self.get_right_sub_tree(del_node) is None:
                return self.remove_one_child(del_parent, del_node)

            else:
                return self.remove_two_children(del_node)
