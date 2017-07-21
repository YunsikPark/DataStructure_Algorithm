from binary_tree import BinaryTree


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
            if data < self.get_node_data(cur):
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

    # def remove_left_sub_tree(self, cur):
    #     del_node = self.get_left_sub_tree(cur)
    #     self.make_left_sub_tree(cur, None)
    #     return del_node
    #
    # def remove_right_sub_tree(self, cur):
    #     del_node = self.get_right_sub_tree(cur)
    #     self.make_right_sub_tree(cur, None)
    #     return del_node

    def remove_leaf(self, parent, del_node):
        # 루트 노드 지울 때
        if del_node == self.get_root():
            self.set_root(None)
            return del_node

        if self.get_left_sub_tree(parent) is del_node:
            self.make_left_sub_tree(parent, None)
        else:
            self.make_right_sub_tree(parent, None)
        return del_node

    def remove_one_child(self, parent, del_node):
        # 루트 삭제
        if del_node is self.get_root():
            if self.get_left_sub_tree(del_node):
                self.set_root(self.get_left_sub_tree(del_node))
            else:
                self.set_root(self.get_right_sub_tree(del_node))
            return del_node

        del_child = None

        if self.get_left_sub_tree(del_node):
            del_child = self.get_left_sub_tree(del_node)
        else:
            del_child = self.get_right_sub_tree(del_node)

        if self.get_left_sub_tree(parent) is del_node:
            self.make_left_sub_tree(parent, del_child)
        else:
            self.make_right_sub_tree(parent, del_child)
        return del_node

    def remove_two_children(self, del_node):
        rep_parent = del_node
        replace = self.get_left_sub_tree(del_node)

        while self.get_right_sub_tree(replace):
            rep_parent = replace
            replace = self.get_right_sub_tree(replace)

        temp_data = self.get_node_data(replace)
        self.set_node_data(replace, self.get_node_data(del_node))
        self.set_node_data(del_node, temp_data)

        if self.get_left_sub_tree(rep_parent) == replace:
            self.make_left_sub_tree(rep_parent, self.get_left_sub_tree(replace))
        else:
            self.make_right_sub_tree(rep_parent, self.get_left_sub_tree(replace))

        return replace

    def remove(self, target):
        del_parent = self.get_root()
        del_node = self.get_root()

        while True:
            if del_node is None:
                return None

            if target is self.get_node_data(del_node):
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


if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    f = lambda x: print(x, end=' ')

    # 전위 순회
    bst.preorder_traverse(bst.get_root(), f)
    print("")

    # remove -1 : 리프 노드 일 때
    # bst.remove(9)

    # remove -2 : 자식 노드 하나 일 때
    # bst.remove(8)

    # remove -3 : 자식 노드가 두개 일 때
    bst.remove(6)

    bst.preorder_traverse(bst.get_root(), f)
    print("")
