class DocumentWithHistory:
    def __init__(self, name):
        # TODO: Add init routine
        # HINT: Initialize undo stack and text contents here
        self.doc_string = ""
        self.history_cmd_data = []
    
    def write(self, text, no_undo=False):
        # TODO: Add write routine
        if not(no_undo):
            self.history_cmd_data.append((self.delete, len(text)))
            
        self.doc_string += text

    def delete(self, char_len, no_undo=False):
        # TODO: Add delete routine
        if len(self.doc_string) >= char_len:
            if not(no_undo):
                self.history_cmd_data.append((self.write, self.doc_string[-char_len:]))
                
            self.doc_string = self.doc_string[:len(self.doc_string)-char_len]

    def clear(self, no_undo=False):
        # TODO: Add clear routine
        if not(no_undo):
            self.history_cmd_data.append((self.write, self.doc_string))
            
        self.doc_string = ""

    def newline(self, no_undo=False):
        # TODO: Add newline routine
        if not(no_undo):
            self.history_cmd_data.append((self.delete, 1))
 
        self.doc_string += "\n"

    def undo(self):
        # TODO: Add undo routine
        if len(self.history_cmd_data) > 0:
            cmd, data = self.history_cmd_data.pop(-1)
            cmd(data, no_undo = True)
        
        pass
    
    # HINT: An undo is just the "antonym" or opposite of
    #       a certain command. For example, if we write()
    #       something, then its undo counterpart would be
    #       delete(). From this observation, you can see that
    #       the document commands will need to push a command
    #       opposite to the undo stack before editing the text
    #       itself.
    
    # HINT: You can add a function __str__(self) that
    #       returns the document contents so that
    #       you can do print(doc), with doc being
    #       an object of type DocumentWithHistory

def main():
    t = int(input())

    for i in range(t):
        n_cmd = int(input())
        doc_name = input()
        docs = DocumentWithHistory(doc_name)
        
        # HINT: Create a new DocumentWithHistory here

        # TODO: Process commands
        for _ in range(n_cmd):
            cmd = input()
            string_cmd_args = cmd.split(maxsplit=1)

            if len(string_cmd_args) == 1:
                if cmd == "x":
                    docs.clear()
                elif cmd == "n":
                    docs.newline()
                elif cmd == "u":
                    docs.undo()
            else:
                cmd, args = string_cmd_args
                if cmd == "w":
                    docs.write(args) 
                elif cmd == "d":
                    docs.delete(int(args))

        # TODO: Print output
        print(f"Case #{i + 1}: Document Name: {doc_name}")
        print(docs.doc_string)



if __name__ == '__main__':
    main()