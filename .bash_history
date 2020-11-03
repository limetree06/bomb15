ls
cd process.c
vi process.c
cd 3-2/OS/uni20171143_uni20181281/project2-1/pintos/src/userprog'
cd 3-2/OS/uni20171143_uni20181281/project2-1/pintos/src/userprog
cd build
make
cd ..
ls
git add process.c
git commit -m "building up the stack"
git push origin master
ls;
cd userprog
ls
cd build
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/args-many -a args-many -- -q  -f run 'args-many a b c d e f g h i j k l m n o p q r s t u v'
ls
cd userprog
ls
cd build
make
int word_align;
    int lenght = 0;
    int sublen=0;
    for(i=0;file_name[i]!=NULL;i++){
    s[i] = file_name[i];
    }
    *esp = PHYS_BASE;
    *esp = *esp - len;
    
    //word_align
    word_align = 4 - len%4;
    if(len%4 != 0) *esp = *esp - word_align;
    //top of argv
    *esp = *esp - 4;
    *(int *)*esp = 0;
    // back to bottom of argv[i][....]
    *esp = PHYS_BASE;
    *esp = *esp - len;
    i=0;
    
    //building stack
    for (token = strtok_r (s, " ", &save_ptr); token != NULL; token = strtok_r (NULL, " ", &save_ptr)){
        // push argv[i][....] from bottom to top
        length = strlen(token);
        strlcpy(*esp, token, length + 1);
        // go to argv[i] and push argv[i]
        *esp = *esp - 4 - word_align - 4*(count - i) - sublen; 
        *(uint32_t **)*esp = (uint32_t *)*esp;
        //back to argv[i][....]
        *esp = *esp + word_align + 4 + 4*(count - i) + sublen;
        //back to argv[i+1][...]
        *esp = *esp + length + 1;
        sublen +=length;
        i++;
    }
        //argv
        *esp = *esp - len - word_align - 4*(count +1)-4;
         *(char **)*esp = *esp + 4;
         //argc
          *esp = *esp - 4;
          *(int *)*esp = count;
          //return address
          *esp = *esp - 4;
          *(int *)*esp = 0;
      }int word_align;
    int lenght = 0;
    int sublen=0;
    for(i=0;file_name[i]!=NULL;i++){
    s[i] = file_name[i];
    }
    *esp = PHYS_BASE;
    *esp = *esp - len;
    
    //word_align
    word_align = 4 - len%4;
    if(len%4 != 0) *esp = *esp - word_align;
    //top of argv
    *esp = *esp - 4;
    *(int *)*esp = 0;
    // back to bottom of argv[i][....]
    *esp = PHYS_BASE;
    *esp = *esp - len;
    i=0;
    
    //building stack
    for (token = strtok_r (s, " ", &save_ptr); token != NULL; token = strtok_r (NULL, " ", &save_ptr)){
        // push argv[i][....] from bottom to top
        length = strlen(token);
        strlcpy(*esp, token, length + 1);
        // go to argv[i] and push argv[i]
        *esp = *esp - 4 - word_align - 4*(count - i) - sublen; 
        *(uint32_t **)*esp = (uint32_t *)*esp;
        //back to argv[i][....]
        *esp = *esp + word_align + 4 + 4*(count - i) + sublen;
        //back to argv[i+1][...]
        *esp = *esp + length + 1;
        sublen +=length;
        i++;
    }
        //argv
        *esp = *esp - len - word_align - 4*(count +1)-4;
         *(char **)*esp = *esp + 4;
         //argc
          *esp = *esp - 4;
          *(int *)*esp = count;
          //return address
          *esp = *esp - 4;
          *(int *)*esp = 0;
      }make
mak
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
cd 3-2/OS/uni20171143_uni20181281/project2-1/pintos/src/userprog
git add process.c
git commit -m "done with building up the stack hopefully"
git push -u
git checkout master
git push -u
git pull
git push -u
ls
git add process.c
git -m commmit "hopefullt well done with building up th stack"
git commmit -m "hopefullt well done with building up th stack"
git commit -m "hopefullt well done with building up th stack"
git pull
git commit -m "hopefullt well done with building up th stack"
git push -u
git branch
cd ..
cd .
cd ..
ls
cd ..
git checkout project-1
ls
git checkout project2-1
git commit -m "message"
git add
git add .
git status
git pull
git add process.c
ls
cd 3-2/OS/uni20171143_uni20181281/project2-1/pintos/src/userprog
cd project2-1
ls
cd pinot
cd pintos
cd src
cd userprog
ls
cd build
make
cd ..
git add process.c
git commit -m
git commit -m "hey come on commit"
git push -u
t push
git pull --rebase
cd ..
git merge project2-1
mkdir project2-1
git add project2-1
git commit –m “Project 2-1 initial commit”
git commit -m "stack"
git push origin master
cd project2-1
ls
cd pintos
ls
cd src
ls
cd userprog
git add process.c
git commit -m "building up the stack"
git push origin master
git add
git commit -a
git pull
git fetch origin
cd ..
git fetch origin
git rm project2-1/pintos/src/userprog/process.c
git add project2-1/pintos/src/userprog/process.c
git add project2-1/pintos/src/userprog/shutdown.c
ls
cd project2-1
ls
cd pinot
cd pintos
ls
cd src
ls
cd userprog
ls
cd ..
git rm project2-1/pintos/src/userprog/shutdown.c
git commit
git merge origin/master
git pull origin master
git status
git commit -am '커밋메시지'
git pull
git push origin/master
git push originvmaster
git push origin master
ls
ccd project2-1
ls
cd project 2-1
ls
cd project2-1
ls
cd pinot
cd pinots
cd pintos
cd src
ls
cd userprog
ls
vi process.c
rm process.c
ls
vi process.c
dc27dc8d314deaa200e27de0b9f783e2531b6f99
vi process.c
cd ..
cd //
cd ..
;s
cd
cd 3-2/OS/uni20171143_uni20181281
git clone cd 3-2/OS/uni20171143_uni20181281
git clone git@gitlab.com:2020-Fall-Operating-System/uni20171143_uni20181281.git
ls
cd projct2-1
cd project2-1
ls
cd pinots
cd pintos
ls
cd sr
cd src
ls
cd userptog
cd userprog
ls
cd build
make
cd ..
git clone git@gitlab.com:2020-Fall-Operating-System/uni20171143_uni20181281.git
ls
cd project2-1
ls
cd pintos
ld
ls
cd src
ls
cd userprog
ls
cd buils
cd build
make
cd ..
vi process.c
ls
ls
cd userprog
ls
cd build
cd
cd 3-2/OS/uni20171143_uni20181281/project2-1/pintos/src/userprog
ls
cd build
make
cd 3-2/OS/uni20171143_uni20181281/project2-1/pintos/src/userprog
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
ls
cd userprog
ls
cd build
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run '/bin/ls -l foo bar'pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run '/bin/ls -l foo bar'pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run '/bin/ls -l foo bar'pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run '/bin/ls -l foo bar'smake
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run '/bin/ls -l foo bar'
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
cd userprog
ls
cd build
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
makw
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
cd ..
grep hex_dump -R
ls
cd userprog
ls
cd build
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
ls
cd 3-2/OS/uni20171143_uni20181281/project2-1/pintos/src/userprog
git pull
cd ..
git pull
git stash
git pull
ls
cd userprog
ls
cd build
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make check
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
ls
cd userprog
ls
cd buil
cd build
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
amek
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make check
make
make check
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
make check
cd 3-2/OS/uni20171143_uni20181281
git pull
git stash
git pull
cd 3-2/OS/uni20171143_uni20181281/project2-1/pintos/src/userprog
ls
cd project2-1
ls
cd pintos
ls
cd src
ls
cd userprog
ls
cd build
ls
make
ls
cd userprog
ls
cd build
make
make check
ls
cd userprog
ls
cd buil
cd build
make
make check
make
make check
ls
cd userprog
ls
cd build
make
make check
make
make check
oid halt (void){ shutdown_power_off();}
void exit (int status){
  printf("%s: exit(%d)\n",thread_name(), status);
  thread_exit();
}
int write (int fd, const void *buffer, unsigned size){
  if (fd == 1){
    putbuf(buffer, size);
    return size;
  }
  //Else, write size bytes from buffer to the file opened with fd, return size
  else return -1; 
}
bool create (const char *file, unsigned initial_size){
  filesys_create (file, initial_size);
}
int open (const char *file){
  struct file* openfile = filesys_open(file);
  if(file == NULL) return -1;
  else{
  }
}
void close (int fd){
  close (fd);
  return 
make check
make
make check
make
make check
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make
ls
cd 3-2/OS/uni20171143_uni20181281
ls
git add project2-1
git commit -m "open..."
git push origin master
ls
lsls
ls
cd userprog
ls
cd build
make
mak
make
ls
cd userprog
ls
cd build
ls
make
make check
make
make check
make
make check
make
make check
make
make check
make
mak
make
make check
make
make check
make
pintos -v -k -T 60 --bochs --filesys-size=2 -p ../../examples/echo -a echo -- -q -f run 'echo x'
make chekc
make
make check
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-missing -a open-missing -- -q  -f run open-missing
make
ㅡ맏
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-missing -a open-missing -- -q  -f run open-missing
make check
make
make check
make
make check
make cjeck
make check
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-missing -- -q  -f run open-empty
make
make check
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-missing -- -q  -f run open-empty
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-boundary -- -q  -f run open-boundary
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-bad-ptr -- -q  -f run open-bad-ptr
make
make check
make
make check
make
make check
make
make check
make
make check
make
make check
make
make check
make
make check
make
make check
make
make check
make
make check
make
make check
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-missing -- -q  -f run open-empty
ls
cd build
cd userprog
ls
cd build
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
make check
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-boundary -- -q  -f run open-boundary
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-boundary -- -q  -f run open-boundary
make
make check
ls
cd tests
ls
cd userprog
ls
vi open-empty.errors
vi open-empty.result
ls
cd userprog
ls
cd build
ls
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
ls
cd build
cd userprog
ls
cd build
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
make check
make
make check
make
make check
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
make check
make
make check
make
make check
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a  open-empty -- -q  -f run open-empty
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
ls
cd userprog
ls
cd build
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
make check
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make check
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make check
make
make check
make
make check
make
make check
make
make check
make
make check
make
make check
make
make check
make
make check
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
  exit(-1);
}
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
make check
make
make check
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a create-normal -- -q  -f run create-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a create-normal -- -q  -f run create-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a create-normal -- -q  -f run create-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a create-normal -- -q  -f run create-normal
make
make check
make
make check
make
make check
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a create-empty -- -q  -f run create-empty
make
ls
cd tests
ls
cd userprog
ls
cd close-stdin.errors
vi close-stdin.errors
vi close-stdin.o
vi close-stdin.d
vi close-stdin.result
vi close-twice.result
vi close-normal.result
vi create-normal.result
cd ..
cd userptog
cd userprog
ls
cd build
make
make check
cd tests
cd userprog
cd ..
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-norma
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
make check
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a open-normal -- -q  -f run open-normal
make
make check
make
make check
make
make check
make
make check
make
make check
make
make check
cd 3-2/OS/uni20171143_uni20181281
ls
git add project2-1
git -m commit "we can do it :)"
git commit -m "we can do it :)"
git push origin master
cd 3-2/OS/uni20171143_uni20181281
git add project2-1
ls
cd userprog
ls
cd build
make
make check
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a create-null -- -q  -f run create-null
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a create-null -- -q  -f run create-null
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-twice -- -q  -f run close-twice
make check
make
make check
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-twice -- -q  -f run close-twice
make
 -S kernel.o kernel.bin
[cs20171143@uni06 build]$ 
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
pintos -v -k -T 60 --bochs  --filesys-size=2 -p tests/userprog/open-empty -a close-normal -- -q  -f run close-normal
make
make check
make
make check
make
make check
make
make check
make
make check
ls
cd 3-2/OS
ls
cd uni20171143_uni20181281
ls
git checkout project2-1
ls
git checkout project2-1
git stash
git checkout project2-1
git clone git@gitlab.com:2020-Fall-Operating-System/uni20171143_uni20181281.git
ls
cd project2-1
ls
cd pinto
cd pintos
ls
cd src
ls
cd userprog
ls
cd build
make
ls
make
cd ..
ls
cd ..
ls
cd ..
ls
rm -rf project2-1
ls
git clone
git clone git@gitlab.com:2020-Fall-Operating-System/uni20171143_uni20181281.git
rm -rf uni20171143_uni20181281
ls
git checkout master 
git merge project2-1
mkdir project2-1
ls
/project2-1/pintos/src/userprog
cd 3-2/OS/uni20171143_uni20181281
git pull
cd ..
cd 3-2/OS/uni20171143_uni20181281/project2-1/pintos/src/userprog
cd
cd 3-2/OS/uni20171143_uni20181281/project2-1/pintos/src/userprog
cd build
ls
cd ..
ls
cd userprog
ls
make
ls
cd build
make check
cd ..
ls
cd userprog
ls
cd ..
ls
cd ..
ls
cd userprog
ls
cd build
make
make check
make
make check
make
make check
make
make check
cd 3-2/OS
ls
cd uni20171143_uni20181281
ls
cd project2-1
ls
vi project2_design_document.txt
cd ..
git add project2-1
git commit -m "add B1, B2"
git push origin master
