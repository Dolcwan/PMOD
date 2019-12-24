import os    
import sys   
import shutil

class path_parse:
    
    '''
    path_parse(os_form,new_path,path_print,print_col)
    
    
    -----------
    | Inputs: |
    -----------
    
    os_form = 'Windows' or 'Linux' 
    new_path = None (by default)
    path_print = False (by default)
    print_col = False (by default)
        
    '''
    
    def __init__(self,os_form,new_path=None,path_print=False,print_col=False):
        
        '''
        --------
        | init |
        --------
        
        Inputs:
        os : 'Windows' or 'Linux'/'Unix'
        new_path = None (by default)
        path_print = False (by default)
        print_col  = False (by default)
        
        .path : A string of the path in which the script is run
        .path_list : A list of strings with values of the directory hiearchy in .path
        .path_head : A string containing the primary (home) directory
        .path_contain : A list of strings with values of the contents of .path
        .path_files : A list of string with values of the file (names with file type) in .path   
        
        .os:  A string to specify the operating system, this determines the path file format 
        .col: True for color Escape code when printing, False by default
        
        '''
        
        global delim
        global color
        
        self.os = os_form
        os_list = ['Ubuntu','Xubutnu','Redhat','Debian','Fedora','MintOS']
        if(self.os in os_list):
            self.os = 'Linux'
        
        if(self.os == 'Windows'):
            delim = '\\'
        elif(self.os == 'Unix' or self.os == 'Linux'):
            delim = '/'
        else:
            delim = ':'
            
        self.col = print_col
        color = self.col
        
        if(new_path != None):            
            self.path = new_path
            if(self.os == 'Windows'):
                self.path_list = self.path.split(delim)
                self.path_head = self.path.split(delim)[0]
            else:
                self.path_list = self.path.split(delim)
                self.path_list = self.path_list[1:]
                self.path_head = self.path_list[0]
            self.path_contain = os.listdir(self.path)
            self.path_files = self.get_path_files()
            self.path_print = path_print
        else:
            self.path = os.getcwd()
            if(self.os == 'Windows'):
                self.path_list = self.path.split(delim)
                self.path_head = self.path.split(delim)[0]
            else:
                self.path_list = self.path.split(delim)
                self.path_list = self.path_list[1:]
                self.path_head = self.path_list[0]
            self.path_contain = os.listdir(self.path)
            self.path_files = self.get_path_files()
            self.path_print = path_print

    
    def documentation(self,string):
        """
        ---------------
        | Description |
        ---------------
        
        path_parse is a class to call commands within python scripts allowing 
        functionality in the image of Linux command-line inputs for file and folder
        functions. The main function in the class is 'cmd' : path_parse.cmd(). This 
        function allows commands to be passed which, return the contents of the current 
        stored directory string, change the current stored directory string, move files 
        between directories and delete files and directories. The class allows for 
        pathway information to be stored and returned as string objects. 
        
	    
        ------------------------
        | Function guidelines: |
        ------------------------
	    
        1) Path functions read and modify from the class stored path variables
        2) Non-Path functions take full pathways and perform file and pathway manipulations 
           from these complete and input pathways.
        3) Path functions contain the word 'Path' in the name, Non-Path functions do not.
        4) Non-Path functions should not rely on the class current (path)way nor on any 
           path class variables.
        5) Path functions should return a boolean value dependent on the success of the operation,
           any values they modify should be self. variables, eliminating the need for returning values.
        6) Non-Path functions should return a boolean value when their operation does not 
           require a value to be returned (e.g. moving, copying or deleting objects) which is 
           dependent on the success of the operation. 
        7) For each Path operation available through the 'cmd' function, there should be a corrosponding
           means of accomplishing the same take through a Non-Path function. 
	    
        Function guideline summary:
	    
        1) Complete interdependence for Path functions
        2) Complete independence for Non-Path functions 
        3) Strict naming scheme to distinguish Path from Non-Path functions
        4) Path Variable restrictions 
        5) Return restrictions on Path functions (Boolean only) 
        6) Return restrictions on Non-Path functions 
        7) Corrospondance in operation between Path and Non-Path functionality      
	    
        ------------------
        | Function List: |
        ------------------

        convention: 

        * path : designates a function which modifies the path variables
        * trac : designates a function which modifies an input path, does not affect path variables.
	    
        
        __init__(self,os_form,new_path=None,path_print=False,print_col=False) : 

                                    Initalizing function, sets path variables

        __cmd_input_parse__(self,string) : 
                          
                                    Parses input strings for the 'cmd' function, 
                                    converts input string to tuple of length 3.

        join_node(self,old_path,new_node) : 

                                    Adds the file or folder name in 'new_node' to
                                    the pathway in 'old_path'. Input and output 
                                    are strings 
        
        create_trac(self,path_list) : 
   
                                    Creates and returns a pathway string from a pathway list
         
        
        get_path_files(self,style = None) : 

                                    Returns a list of strings corrosponding to the names
                                    of the files, whose names contains file extensions,
                                    in the current (path) directory, option for selection 
                                    by extension.
	    
        move_file(self,file_name,new_location,upbool = False) : Moves 'file_name' to 'new_location', 
                                                                note that 'file_name' must be a file
                                                                with a file extension in the string
                                                                and 'new_location' must be a folder,
                                                                both must be in the current directory.
                                                                if 'upbool' is True, then the file is 
                                                                moved to the higher directory and the
                                                                location in 'new_location' is ignored.
        
        del_file(self,file_name) : Deletes file with a name equal
                                   to 'file_name' in the current
                                   (path) directory
        
        create_dir(self,dir_name) : Creates a folder with a name 
                                    equal to 'dir_name' in the 
                                    current (path) directory
        
        find_file(self,file_name,pathway=None,pathopt = False,files=True,sort=str) : 

                                   Checks the current (path) directory for a file with 
                                   'file_name' as its identifier. Returns boolean.
	    
        grep_file(self,fragment,pathway=None,pathopt = False,files=True,sort=str) :

                                   Checks the current (path) directory for any file with
                                   'fragment' in its name. The list of matching file names 
                                   is returned in string format. 
                                     
        __fancy_print__(self,col=False) : Prints the current (path) directory pathway in a
                                      stylized format. 
	    
        __fancy_print_list__(self,array) :  Prints a list, 'array', in a stylized format.
	    
        """

        cd_list = ['ls','pwd','dir','cd','chdir','mv','rm','mkdir',
                   'rmdir','find','grep','help','vi']

        action_list = ["Usage: ['ls',..,..] , returns a list of strings corrosponding to content of path directory",
                       
                       "Usage: ['pwd',..,..] , returns a string corrosponding to the pathway for path directory",
                       
                       "Usage: ['dir',['file1.file','file2.file'],..] , returns list of strings corrosponding "+
                       "to pathways of grouped files",
                       
                       "Usage: ['cd',..,pathway] , returns None, modifies the path variables to move from the "+ 
                       "path directory to that specified in the pathway. The value for pathway may be either "+
                       "{'..' to move up one directory, '~' to move to home, or a name of a subdirectory}",
                       
                       "Usage: [chdir,..,full_pathway] , returns None, moves path variables to move from the "+
                       "current directory to that specified by full_pathway, full_pathway must be a full pathway",
                       
                       "Usage: [mv,['file1.file','file2.file'],destination] , returns None, moves files in path "+
                       "directory to the destination directory.",
                       
                       "Usage: [rm,['file1.file','file2.file'],..] , returns None, removes files in path directory", 
                       
                       "Usage: [mkdir,['fold1','fold2'],..] , returns None, creates folders in path directory",
                       
                       "Usage: [rmdir,['fold1','fold2'],..] , returns None, deletes folders and content in path directory",                             
                       "Usage: [find,['file1.file','file2.file'],..] , returns dictionary, searches for files by name, "+
                       " and returns a dictionary with boolean values for the existance of the files",
                          
                       "Usage: [grep,['file1.file','file2.file'],..] , returns dictionary, searches for fragments, "+
                       " and returns a dictionary with boolean values for the files containing searched fragments",

                       "Usage: [help,['command'],..] , returns either a list or string, "+
                       "if no command is specified, 'help' returns a list of possible commands, else if a "+
                       "command is specified a string describing the commands usage is returned",
                         
                       "Usage: [grep,['file1.file','file2.file'],..] , returns dictionary, searches for fragments, "+
                       " and returns a dictionary with boolean values for the files containing searched fragments", 
                      ]   

#        help_dict = {k: v for k, v in zip(cd_list,action_list)}        
        help_dict = dict(zip(cd_list,action_list))  # Added for backward compatability
        
        single_command_list = ['ls', 'pwd'] 
        single_path_list_nogroup = ['cd','chdir','vi','help']
        single_path_list_group = ['rm','rmdir','mkdir','dir','find','grep']
        double_path_list = ['mv']
                 
        if(string == 'help'):
            return help_dict
        elif(string == 'single_cmd'):
            return single_command_list
        elif(string == 'single_ng_cmd'):
            return single_path_list_nogroup
        elif(string == 'single_gp_cmd'):
            return single_path_list_group
        elif(string == 'double_cmd'):
            return double_path_list
         
         
        
         
    def __cmd_input_parse__(self,string):
        '''
        -----------------------
        | __cmd_input_parse__ |
        -----------------------
        
        Inputs:

        string : a string, formatted for use in the .cmd() function 
         
        output:
         
        out_inst : a tuple formatted for parsing in the .cmd() function
        
        '''
    
        def combine_list_str(array, span, ignore=None, space=False):
            
            out_string = ''
            count = 0
            if(ignore != None):
                for i in array:
                    if(count not in ignore):
                        if(space):
                            if(count<len(array)-len(ignore)-1):
                                out_string = out_string+i+' '
                            else:
                                out_string = out_string+i
                        else: 
                            out_string = out_string+i   
                    count+=1
                return out_string
            else: 
                if(span[1] == 'End' or span[1] == 'end' or span[1] == '' or span[1] == -1):
                    abridged_list = array[span[0]:]
                else:
                    abridged_list = array[span[0]:span[1]]
                   
                count = 0
                for i in abridged_list:
                    if(space):
                        if(count<len(abridged_list)-1):
                            out_string = out_string+i+' '
                        else:
                            out_string = out_string+i                        
                    else:  
                        out_string = out_string + i
                    count+=1
                return out_string
    
        if(not isinstance(string,str)): 
            print("Error: input must be a string, not a "+str(type(string)))
            return ('',[],'')
        
        single_command_list = ['ls', 'pwd'] 
        single_path_list_nogroup = ['cd','chdir','vi','help']
        single_path_list_group = ['rm','rmdir','mkdir','dir','find','grep']
        double_path_list = ['mv']
                                                                   
        string_list = string.split(" ")
        string_list = filter(lambda l: l != '',string_list)            
        cmd_inst = string_list[0]
        nstr = len(string_list)
        
        if(cmd_inst in single_command_list):
            out_inst = (cmd_inst,[],'')
            return out_inst
    
        if(cmd_inst in single_path_list_nogroup):               
            out_inst_str = combine_list_str(string_list,[1,'End'],space=True)
            if(cmd_inst != 'vi'):
                out_inst = (cmd_inst,[],out_inst_str)
            else:
                out_inst = (cmd_inst,[out_inst_str],'')
            return out_inst                     
        
        if(cmd_inst in single_path_list_group):
            if(';' in string):
                inst_str = combine_list_str(string_list,[1,'End'],space=True)
                out_inst_list = inst_str.split(';')
                out_inst_list = filter(lambda l: l != '',out_inst_list)
                out_inst = (cmd_inst,out_inst_list,'')
                return out_inst
            else:
                out_inst_str = combine_list_str(string_list,[1,'End'],space=True)
                out_inst = (cmd_inst,[out_inst_str],'')
                return out_inst 
    
        if(cmd_inst in double_path_list):
            if(';' in string):
                dest_list = []
                while(';' not in string_list[-1]):
                    dest_list.append(string_list.pop(-1))
                dest_list = dest_list[::-1]
                dest_str = combine_list_str(dest_list,[0,'End'],space=True)
                inst_str = combine_list_str(string_list,[1,'End'],space=True)
                out_inst_list = inst_str.split(';')
                out_inst_list = filter(lambda l: l != '',out_inst_list)
                out_inst = (cmd_inst,out_inst_list,dest_str)
                return out_inst
            else:
                if(len(string_list) == 3):
                    out_inst = (cmd_inst,[string_list[1]],string_list[2])
                elif('.' in string):
                    dest_list = []
                    while('.' not in string_list[-1]):
                        dest_list.append(string_list.pop(-1))
                    print(string_list)
                    dest_list = dest_list[::-1]
                    dest_str = combine_list_str(dest_list,[0,'End'],space=True)
                    inst_str = combine_list_str(string_list,[1,'End'],space=True)
                    out_inst = (cmd_inst,[inst_str],dest_str)
                else:
                    print("Error: The input spaceing created ambiguity for the indexer: '"+string+"'")
                    raise IndexError  
                
                return out_inst

        print("Error: command +'"+cmd_inst+"' not recognized, use 'help' to view available functions")
        return None 
    
                             
    def join_node(self,old_path,new_node):
        output = old_path+delim+new_node
        return output
            
        
    def create_trac(self,trac_in,node_add=None,insort='list',outsort='str'):        
        '''
        
        ---------------
        | create_trac |
        ---------------

        if(insort == 'list')
        
            Input: 'trac_in': [list,tuple], A path-formatted list             
            Return: 'trac_out': [string], a path-formatted string

        if(insort == 'str')

                'trac_in': [list,tuple], A path-formatted list 
                'trac_out': [string], a path-formatted string
            
        Description: Formats a path-formatted list into a path-formatted string
                     options to add a node and format return in both string and list 
        
        '''
        trac_out = ''
        count = 0

        if(insort == 'list'):

            while('' in trac_in):
                trac_in.remove('')
            for i in trac_in:
                if(count == 0):
                    trac_out = str(i) 
                else:
                    trac_out = self.join_node(trac_out,i)
                count+=1
            
            if(self.os == 'Unix' or self.os == 'Linux'):
                trac_out = '/'+trac_out
             
            if(outsort == 'list'):
                trac_out = trac_out.split(delim)
                trac_out = filter(lambda l: l != '',trac_out)                 
             
        elif(insort == 'str'):
            if(outsort == 'list'):
                trac_out = trac_out.split(delim)
                trac_out = filter(lambda l: l != '',trac_out)                         

        return trac_out            
        
        
    def get_path_files(self,style = None):
        '''
        ------------------
        | get_path_files |
        ------------------
        
        Input: 
        
            'style': [string], (default value: None), A string corrosponding to 
                                                      a file extension type.
        
        Return:
         
            'file_list': [list], A list of strings corrosponding to all the files
                                 in the current (path) directory matching the 
                                 'style' extension, if 'style' == None, then all
                                 file names are included in 'file_list'
            
        Description: Returns a list of strings corrosponding to the file names in 
                     the current (path) directory, option for selecting only a 
                     specific file extension. 
        
        '''
        current_folder_content = self.path_contain
        file_list = []
        if(style == None):
            for i in current_folder_content:
                if('.' in i):
                    file_list.append(i)
        else:
            for i in current_folder_content:
                file_type = '.'+style
                if(file_type in i):
                    file_list.append(i)
        return file_list
    

    def update_path(self,path_updater,sort):        
        '''
        
        ---------------
        | update_path |
        ---------------
        
        Input: 
        
            'path_updater': [list,tuple], A path-formatted list ]
            'sort'        : [type]      , A python data-type
                    
        Description: Formats a path-formatted list into a path-formatted string,
                     the new path then replaces the old path directory along with 
                     replacing the old path variables with those of the new path.
        
                
        '''
        if(sort == list):
            self.path_list = path_updater
            self.path = self.create_trac(path_updater)
            if(self.os == 'Windows'):                    
                if(self.path == self.path_head):
                    self.path = self.path+'//'
            self.path_contain = os.listdir(self.path)
            self.path_files = self.get_path_files()   
            return True
        elif(sort == str):
            self.path = path_updater
            self.path_list = self.path.split(delim)
            if(self.os == 'Windows'):                    
                if(self.path == self.path_head):
                    self.path = self.path+'//'
            self.path_contain = os.listdir(self.path)
            self.path_files = self.get_path_files() 
            return True
        else:
            print("[update_path] Error: 'sort' not a valid type")
            return False 
        
        
    def climb_path(self,up_dir_inst,exit):
        if(up_dir_inst in self.path_list):
            spl_copy = list(self.path_list)
            new_path_list = []
            switch = True
            for i in spl_copy:
                if(i != up_dir_inst and switch == True):
                    new_path_list.append(i)
                else:
                    switch = False
            new_path_list.append(up_dir_inst)
            if(exit == 'list'):
                output = new_path_list
                return output
            elif(exit == 'str'):
                output = self.create_trac(new_path_list)
                return output
            elif(exit == 'update'):                
                output = self.update_path(new_path_list,list)
                return output
            else:
                print("[climb_path] Error: 'exit' command: '"+str(exit)+"' not recongized")
        else: 
            print("[climb_path] Error: Directory "+up_dir_inst+" not found in current (path) hierarchy")
            return False
        
    
    def get_trac_contain(self,path,sort = str,rtrn = 'all'):
        
        if(sort == str):
            new_path = path
        elif(sort == list):
            new_path = self.create_trac(path)
        else:
            print("[get_trac_contain] Error: 'sort' option must be either 'str' or 'list'; '"
                  +str(sort)+"' is invalid")
        
        content = os.listdir(new_path)
        
        if(rtrn == 'all'):
            return content
        elif(rtrn == 'files'):
            files = []
            for i in content: 
                if('.' in i): files.append(i)
            return files
        elif(rtrn == 'folders'):
            folders = []
            for i in content: 
                if('.' not in i): folders.append(i)
            return folders            
        else:
            print("[get_trac_contain] Error: 'rtrn' input; '"+rtrn+"' , not valid")
            
             
    
    def move_file(self,file_loc,fold_loc,file_sort,fold_sort):
        
        if(fold_sort == list):
            fold_loc = self.create_trac(fold_loc)                
        if(file_sort == list):
            file_loc = self.create_trac(file_loc)
                      
        if(self.os == 'Windows'):                    
            if(fold_loc == self.path_head):
                fold_loc = fold_loc+'//'
                   
        try: 
            shutil.move(file_loc,fold_loc) 
        except: 
            print("[move_file] Error: File could not be moved.")
            print("File pathway: "+file_loc)
            print("Destination pathway: "+fold_loc)
            return False
        
        output = self.update_path(self.path,str)
        return output

    
    def del_file(self,file_loc,update=False):           
        try:
            os.remove(file_loc)
        except:
            print("[del_file] Error: File could not be deleted.")
            print("File pathway: "+file_loc)
            return False
            
        if(update):            
            utest = self.update_path(self.path,str)
            if(utest):
                return utest
            else:
                print("[del_file] Error: path not updated")     
                return False
        else:
            return True

        
    def del_fold(self,fold_loc,sort=str,update=False):
        
        verif = False

        if(sort == str):
            foldtype = isinstance(fold_loc,str)
            if(not foldtype):
                print("[del_fold] Error: input pathway must be a string")
                return False
        elif(sort == list):
            try: 
                fold_loc = create_trac(fold_loc)
            except: 
                print("[del_fold] Error: input pathway could not be parsed into a string")
                return False
        else:
            print("[del_fold] Error: 'sort' is not a valid data type")
            return False
        
        try: 
            content = self.get_trac_contain(fold_loc)
        except:
            print("[del_fold] Error: The pathway "+fold_loc+" did not yield a folder whose content could be accessed")
            return False
        
        for i in content:
            file_path = self.join_node(fold_loc,i)
            if(os.path.isdir(file_path)):
                try:
                    verif = self.del_fold(file_path)
                    if(verif == False):
                        print("[del_fold] Error: the folder at pathway "+file_path+" could not be deleted")
                except: 
                    print("[del_fold] Error: the folder at pathway "+file_path+" could not be deleted")             
            else:
                try:                
                    verif = self.del_file(file_path)
                    if(verif == False):
                        print("[del_fold] Error: the file at pathway "+file_path+" could not be deleted")
                except: 
                    print("[del_fold] Error: the folder at pathway "+file_path+" could not be deleted")  
        try:  
            verif = os.rmdir(fold_loc)
            if(verif == False):
                print("[del_fold] Error: the file at pathway "+fold_loc+" could not be deleted")
        except: 
            print("[del_fold] Error: the folder at pathway "+fold_loc+" could not be deleted") 

        if(verif and update):
            utest = self.update_path(self.path,str)
            return utest
 
        return verif
            
        
                        
    def create_dir(self,inpath,sort=str,update=False):
        if(sort == str):
            pathway = inpath
        elif(sort == list):
            pathway = self.create_trac(inpath)
        else:
            print("[create_dir] Error: sort value: '"+str(sort)+"' not recognized")
            return False
            
        try:
            os.mkdir(pathway)
            if(update):
                utest = self.update_path(self.path,str)
                return utest     
            else:
                return True      
        except:           
            print("[create_dir] Error: a directory could not be created at this pathway")
            print("Pathway : "+pathway)     
            return False 
 
                
    def find_file(self,file_name,pathway=None,pathopt = False,files=True,sort=str):
        
        if(pathopt):
            if(files):
                spf = self.path_files
            else:
                spf = self.path_contain
            if(file_name in spf):
                return True
            else:
                return False
        
        if(sort == str and pathway != None):
            trac = pathway
        elif(sort == list and pathway != None):
            trac = self.create_trac(pathway)
        elif(pathway == None):
            print("[find_file] Error: 'pathway' is empty")
            return False
        else: 
            print("[find_file] Error: check 'pathway' and 'sort'. 'sort' should be either list or str. ")
            return False   

        if(files):
            spf = self.get_trac_contain(trac,rtrn='files')
        else:     
            spf = self.get_trac_contain(trac) 
        if(file_name in spf):
            return True
        else:
            return False            
        

    def grep_file(self,fragment,pathway=None,pathopt = False,files=True,sort=str):

        if(pathopt):
            if(files):
                spf = self.path_files
            else:
                spf = self.path_contain
            grep_list = []
            for i in spf:
                if(fragment in i):
                    grep_list.append(i)
            return grep_list

        if(sort == str and pathway != None):
            trac = pathway
        elif(sort == list and pathway != None):
            trac = self.create_trac(pathway)
        elif(pathway == None):
            print("[grep_file] Error: 'pathway' is empty")
            return False
        else: 
            print("[grep_file] Error: check 'pathway' and 'sort'. 'sort' should be either list or str. ")
            return False   

        if(files):
            spf = self.get_trac_contain(trac,rtrn='files')
        else:     
            spf = self.get_trac_contain(trac) 
              
        for i in spf:
            if(fragment in i):
                grep_list.append(i)
        return grep_list

        
        
    def __fancy_print__(self,col=False):
        
        if(col):
            blue = '\033[38;5;4m'
            black = '\033[38;5;0m'
            if(self.os == 'Unix' or self.os == 'Linux'):
                black = '\033[38;5;2m'
        else:
            blue,black=('','')
        
        nl = '\n'
        atsp = '   '
        headln = nl+'The current pathway is: '+nl
        bodyln = nl+'The content of the current directory is as follows: '+nl 
        
        print(headln)
        print(atsp+self.path)
        
        try: 
            spc = self.path_contain
            spf = self.path_files
        
            print(bodyln)
            for i in spc:
                if(i in spf):
                    print(black+atsp+i)
                else:
                    print(blue+atsp+i)
            print(black)
            return True

        except:
            return False

    
    def __run_fancy_print__(self):
        if(self.path_print):
            try:
                ecrive = __self.fancy_print__(color)         
                return True
            except:
                return False
        else:                        
            return True   
        
            
    def __fancy_print_list__(self,array):

        nl = '\n'
        atsp = '   '
        
        print(nl)
        for i in array:
            print(atsp+str(i))
        print(nl)
        return None
        

    ####################################################    
    # cmd Function: String-to-Command Parsing Function #
    ####################################################
    
    def cmd(self,cmd_string):
        
        '''
        -------
        | cmd |
        -------
        
        Input: 
        cmd_string : a string, must be formated according to the specifications below.
        
        Valid Commands: 
        
        'ls' : returns list of strings containing the contents of the present directory
        'dir': returns pathway for file in the current directory
        'pwd'  : Returns current directory pathway as string; equivalent to 'self.path'
        'cd' : moves into the input directory, note: input directory must be in current directory
               ('..' to move upwards) ('\\' or '/' to specify directory in root directory)
               ('~' moves to home directory)
        'chdir' : moves to the directory input, input must be full directory pathway 
        'mv' : moves file from current directory into subdirectory
               (format note: 'mv file_path.file Directory_Name') [file extension must be included]
        'rm' : remove input file from current directory
        'mkdir' : make new directory with name equalivalent to input string
        'rmdir' : delete subdirectory (equiv. to 'rm -rf Directory_Name')
        'find' : Searches the current directory for the input file string and returns boolean
        'grep' : Searches the current directory for the input pattern and returns list of matches
        'help' : Returns list of valid commands
        
        '''

        ##################
        #  Subfunctions  #
        ##################

        def head_check():                  
            if(len(self.path_list) == 1):
                if(self.path_print):                        
                    print("Warning: No remaining parent directories left")
                return True
            else:
                return False

        def print_func(test):
            success = True
            if(test):
                ptest = self.__run_fancy_print__()
                if(not ptest):
                    success = False 
                    print("Error: An unknown error was raised while attempting to print...")
            else:
                print("Error: Failure while updating current path")
                success = False
            return success
            

        def updater(new_path,sort,success,value):
            utest = self.update_path(new_path,sort)                 
            success = print_func(utest)
            result = (success,value)
            return result


        def cmd_pwd(tup):
            success = True
            cmd_inst, file_list, dest_str = tup
                        
            try:
                value = self.path 
            except: 
                value = None
                success = False
                print("Error: current (path) directory pathway not found")

            success = print_func(success)               
            result = (success,value)                                       
            return result
            
             
        def cmd_ls(tup):
            success = True
            cmd_inst, file_list, dest_str = tup 

            try:
                value = self.path_contain
            except:
                value = None 
                success = False
                print("Error: current (path) directory contents not found")

            success = print_func(success)            
            result = (success,value)
            return result
            
             
        def cmd_dir(tup):
            success = True            
            cmd_inst, file_list, dest_str = tup

            nlist = len(file_list)
            new_file_list = []

            for i in file_list:
                verify = self.find_file(i,pathopt = True)
                if(verify):
                    new_file_list.append(self.join_node(self.path,i))
                else:
                    success = False
                    print("Warning Error: file name, '"+i+"' not found in current (path) directory")
            
            value = new_file_list

            if(self.path_print):
                ptest_1 = self.__fancy_print__()                
                print("Pathway string(s): " )
                ptest_2 = self.__fancy_print_list__(new_file_list)
                if(not ptest_1 and not ptest_2):
                    success = False
                    print("Error: An unknown error was raised while attempting to print...")
            
            result = (success,value)                
            return result
             
                     
        def cmd_cd(tup):
            success = True            
            value = None
            cmd_inst, file_list, dest_str = tup
                                    
            if(dest_str == '..'):                  
                if(head_check()):
                    result = (success,value)
                    return result 
                else:
                    up_path_list = list(self.path_list)[:-1] 
                
                result = updater(up_path_list,list,success,value)
                return result
            
            elif(dest_str in self.path_contain):
                dest_loc = self.join_node(self.path,dest_str)
                if(os.path.isdir(dest_loc)): 
                    new_path_list = list(self.path_list)
                    new_path_list.append(dest_str)
                    utest = self.update_path(new_path_list,list)
                else:
                    success = False 
                    print("Error: '"+dest_loc+"not a valid folder in current (path) directory")
                    print("It appears that '"+dest_loc+"' is a file object or is corrupted")    
                    result = (success,value)
                    return result 

                success = print_func(utest)
                result = (success,value)
                return result
            
            elif(dest_str[0] == '/' or dest_str[0] == '\\'):
                ndir_inst = dest_str[1:]
                ctest = self.climb_path(ndir_inst,'update')
                success = print_func(ctest)
                result = (success,value)
                return result
                    
            elif(dest_str == '~'):                
                ctest = self.climb_path(self.path_head,'update')
                success = print_func(ctest)  
                result = (success,value)
                return result
                
            else:
                print("Error: '"+dest_str+"' not a valid destination")
                success = False
            
            result = (success,value)
            return result
            
            
        def cmd_chdir(tup):
            success = True            
            value = None
            cmd_inst, file_list, dest_str = tup 
            
            try: 
                utest = self.update_path(dest_str,str)
                success = print_func(utest)              
            except:
                print('Error: pathway '+dest_str+' could not be reached')
                success = False 
            
            result = (success,value)
            return result 
            
                
        def cmd_mv(tup,sort='ALL'):
            
            success = True            
            value = None
            cmd_inst, file_list, dest_str = tup  
            all_list = ('ALL','all','All')      
             
            # Format 
            mv_file_list
            for i in file_inst: 
                if(sort == 'File'):
                    if('.' not in file_inst):
                        print('Error: '+file_inst+' is missing type extension')
                        success = False
                    else:
                        mv_file_list.append(i)
                elif(sort == 'Directory' or sort == 'Folder'):
                    if('.' in file_inst):
                        print('Error: '+file_inst+' contains file extension; not a valid directory name')
                        success = False
                    else:
                        mv_file_list.append(i)
                elif(sort in all_list):
                    mv_file_list.append(i)
                else:
                    print("Error: 'sort' option: '"+sort+"' not recognized")
                    success = False
                    result = (success,value)
            
            for i in range(len(mv_file_list)):
                mv_file_list[i] = self.join_node(self.path,mv_file_list[i])
                         
            # Move File                                     
            if(dest_str == '..'):                  
                if(head_check()):
                    result = (success,value)
                    return result  
                else:
                    up_path_list = list(self.path_list)[:-1]

                for i in mv_file_list: 
                    mtest = self.move_file(i,up_path_list,str,list)
                    if(not mtest):
                        success = False 
                        print("Error: contents of this path: '"+i+"' could not be moved")

                result = updater(self.path_list,list,success,value)
                return result     
            
            elif(dest_str in self.path_contain):                
                dest_path_list = list(self.path_list)
                dest_path_list.append(dest_str)  
                     
                for i in mv_file_list:              
                    mtest = self.move_file(i,dest_path_list,str,list)
                    if(not mtest):
                        success = False 
                        print("Error: contents of this path: '"+i+"' could not be moved")
                                     
                result = updater(self.path_list,list,success,value)
                return result  
            
            elif(dest_str[0] == '/' or dest_str[0] == '\\'):
                dest_str = dest_str[1:]
                dest_path_list = self.climb_path(dest_str,'str')

                for i in mv_file_list:              
                    mtest = self.move_file(i,dest_path_list,str,list)
                    if(not mtest):
                        success = False 
                        print("Error: contents of this path: '"+i+"' could not be moved")
                                     
                result = updater(self.path_list,list,success,value)
                return result  
                                      
            elif(dest_str == '~'):                
                dest_path_list = self.climb_path(self.path_head,'list')

                for i in mv_file_list:              
                    mtest = self.move_file(i,dest_path_list,str,list)
                    if(not mtest):
                        success = False 
                        print("Error: contents of this path: '"+i+"' could not be moved")
                                     
                result = updater(self.path_list,list,success,value)
                return result  
            
            else:
                print("Error: The file couldn't be moved...")
                return None                 
            
            
        def cmd_rm(tup):
                      
            success = True            
            value = None
            cmd_inst, file_list, dest_str = tup 
            
            # Format
            
            for i in file_list:   
                if(i in self.path_files):
                    file_path_str = self.join_node(self.path,i)
                    dtest = self.del_file(file_path_str,True)
                    if(not dtest):
                        success = False 
                        print("Error: contents of the path: '"+i+"' could not be deleted")
                else: 
                    success = False 
                    print("Error: '"+i+"' not found within the current (path) directory")
            
                result = updater(self.path_list,list,success,value)
                return result
            

        def cmd_mkdir(tup):
            
            success = True            
            value = None
            cmd_inst, file_list, dest_str = tup      
            
            for i in file_list:
                file_path_str = self.join_node(self.path,i)
                ctest = self.create_dir(file_path_str)  
                if(not ctest):
                    success = False 
                    print("Error: contents of this path: '"+i+"' could not be moved")
                                     
            result = updater(self.path_list,list,success,value)
            return result  

        
        def cmd_rmdir(tup):

            success = True            
            value = None
            cmd_inst, file_list, dest_str = tup   
            
            for i in file_list: 
                if(i in self.path_contain):
                    file_path_str = self.join_node(self.path,i)
                    output = self.del_fold(file_path_str)

            result = updater(self.path_list,list,success,value)
            return result        
        
        
        def cmd_find(tup):

            success = True            
            value = None
            cmd_inst, file_list, dest_str = tup   
            
            found_list = []
            for i in file_list:            
                ftest = self.find_file(i,pathopt = True)
                found_list.append(ftest)

#            found_dict = {k: v for k, v in zip(file_list, found_list)}   
            found_dict = dict(zip(file_list,found_list))
                
            if(self.path_print):
                if(all(i == True for i in found_list)):
                    print("All Files have been found in the current directory!")
                else:
                    for j in found_dict:
                        if(found_dict[j] == False):
                            print("No file named '"+j+"' found in current directory.")
            
            value = found_dict
            result = (success,value)
            return result
          
        
        def cmd_grep(tup):

            success = True            
            value = None
            cmd_inst, file_list, dest_str = tup   
            
            grep_list = []
            for i in file_list:
                gtest = self.grep_file(i,pathopt = True)
                grep_list.append(gtest)

#            grep_dict = {k: v for k, v in zip(file_list, grep_list)} 
            grep_dict = dict(zip(file_list,grep_list))
             
            if(self.path_print):
                for i in file_list:
                    if(len(grep_dict[i]) == 0):
                        print("No matches found for the string, '"+i+"' :")
                    else:
                        print("The following matches were found for the string, '"+i+"' :")
                        self.__fancy_print_list__(grep_dict[i])
                        
            value = grep_dict
            result = (success,value)                       
            return result        
        
        
        def cmd_help(tup):

            success = True            
            value = None
            cmd_inst, file_list, dest_str = tup 

            cd_list = ['ls','dir','pwd','cd','chdir','mv','rm','mkdir',
                       'rmdir','find','grep','help','vi']
            
            help_dict = self.documentation('help')
               
            if(dest_str == ''):
                if(self.path_print):
                    print('Below is a list of valid input commands:\n')
                    self.__fancy_print_list__(cd_list)
                    value = cd_list
                    help_text = "Place command name after 'help' for more info on that command"

            else:
                cmd_val = dest_str
                if(cmd_val in cd_list):
                    help_dict = self.documentation('help')
                    help_text = help_dict[cmd_val]
                else:
                    success = False
                    help_text = "Error: the command '"+cmd_val+"' not recognized"

            if(self.path_print):                   
                print(help_text)
                print('\n')

            value = help_text                                      
            result = (success,value)
            return result   
                
                
            
        ##################
        # Function: Main #
        ##################

        fail_tup = (False,None)
        cmd_tuple = self.__cmd_input_parse__(cmd_string)   
        cmd_inst = cmd_tuple[0]        

        result = fail_tup     
               
        if(cmd_inst == 'pwd'):
            result = cmd_pwd(cmd_tuple)

        elif(cmd_inst == 'ls'):
            result = cmd_ls(cmd_tuple)        

        elif(cmd_inst == 'dir'):
            result = cmd_dir(cmd_tuple)   

        elif(cmd_inst == 'cd'):
            result = cmd_cd(cmd_tuple)

        elif(cmd_inst == 'chdir'):
            result = cmd_chdir(cmd_tuple)

        elif(cmd_inst == 'mv'):    
            result = cmd_mv(cmd_tuple)

        elif(cmd_inst == 'rm'):
            result = cmd_rm(cmd_tuple)      

        elif(cmd_inst == 'mkdir'):
            result = cmd_mkdir(cmd_tuple) 

        elif(cmd_inst == 'rmdir'):
            result = cmd_rmdir(cmd_tuple)

        elif(cmd_inst == 'find'):
            result  = cmd_find(cmd_tuple)

        elif(cmd_inst == 'grep'):
            result = cmd_grep(cmd_tuple)

        elif(cmd_inst == 'help'):
            result = cmd_help(cmd_tuple)

        else:
            spc = '     '
            tup_str = str(cmd_tuple)
            print("Error: Input '"+cmd_string+"' not resolved")
            print("It appears that either 'cmd_string' was not recognized")
            print("Or that, the operand with which it was combined was not properly parsed")
            print("Below is a summary of the output:")
            print("\n")
            print(spc+"'cmd_inst' = '"+cmd_inst+"'")
            print(spc+"'cmd_tuple' = '"+tup_str+"'") 
            print('\n')
            return fail_tup

        (success,value) = result
        
        return result 