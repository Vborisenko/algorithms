class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        paths = list(filter(lambda x: x != "", path.split("/")))
        for path in paths:
            if path == "..":
                if len(path_stack) > 0:
                    path_stack.pop()
            elif path == ".":
                continue
            else:
                path_stack.append(path)
        return "/" + "/".join(list(path_stack))