#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define LOAD_FACTOR 0.7
#define INITIAL_SIZE 100

typedef unsigned int uint;

typedef struct word {
    char *w;
    int count;
    struct word *next;
} unigram;

typedef struct phrase {
    char *p;
    int count;
    struct phrase *next;
} bigram;

typedef struct {
    unigram **table;
    int size;
    int count;
} Unimap;

typedef struct {
    bigram **table;
    int size;
    int count;
} Bimap;

uint hash(const char *key, int size) {
    uint hash = 0;
    while (*key) {
        hash = hash << 5 + *key++;
    }
    return hash % size;
}

void resizeUnimap(Unimap *map) {
    int newSize = map->size * 2;
    unigram **newTable = (unigram **)calloc(newSize, sizeof(unigram *));
    for (int i = 0; i < map->size; i++) {
        unigram *current = map->table[i];
        while (current != NULL) {
            uint newIndex = hash(current->w, newSize);
            unigram *next = current->next;
            current->next = newTable[newIndex];
            newTable[newIndex] = current;
            current = next;
        }
    }
    free(map->table);
    map->table = newTable;
    map->size = newSize;
}

void resizeBimap(Bimap *map) {
    int newSize = map->size * 2;
    bigram **newTable = (bigram **)calloc(newSize, sizeof(bigram *));
    for (int i = 0; i < map->size; i++) {
        bigram *current = map->table[i];
        while (current != NULL) {
            uint newIndex = hash(current->p, newSize);
            bigram *next = current->next;
            current->next = newTable[newIndex];
            newTable[newIndex] = current;
            current = next;
        }
    }
    free(map->table);
    map->table = newTable;
    map->size = newSize;
}

void Uniinsert(Unimap *map, const char *word) {
    if ((float)(map->count + 1) / map->size > LOAD_FACTOR) {
        resizeUnimap(map);
    }
    unigram *newEntry = (unigram *)malloc(sizeof(unigram));
    newEntry->w = strdup(word);
    newEntry->count = 1;
    newEntry->next = NULL;
    uint index = hash(word, map->size);
    newEntry->next = map->table[index];
    map->table[index] = newEntry;
    map->count++;
}

void Biinsert(Bimap *map, const char *phrase) {
    if ((float)(map->count+1)/map->size>LOAD_FACTOR) {
        resizeBimap(map);
    }
    bigram *newEntry=(bigram *)malloc(sizeof(bigram));
    newEntry->p=strdup(phrase);
    newEntry->count=1;
    newEntry->next=NULL;
    uint index=hash(phrase,map->size);
    newEntry->next=map->table[index];
    map->table[index]=newEntry;
    map->count++;
}

void addUniCount(Unimap *map, const char *word) {
    uint index = hash(word, map->size);
    unigram *current = map->table[index];
    while (current != NULL) {
        if (strcmp(current->w, word) == 0) {
            current->count++;
            return;
        }
        current = current->next;
    }
    Uniinsert(map, word);
}

void addBiCount(Bimap *map, const char *phrase) {
    uint index=hash(phrase,map->size);
    bigram *current=map->table[index];
    while (current!=NULL) {
        if(strcmp(current->p,phrase)==0) {
            current->count++;
            return;
        }
        current=current->next;
    }
    Biinsert(map,phrase);
}

Unimap *generateUnimap() {
    Unimap *map = (Unimap *)malloc(sizeof(Unimap));
    map->table = (unigram **)calloc(INITIAL_SIZE, sizeof(unigram *));
    map->count = 0;
    map->size = INITIAL_SIZE;
    return map;
}

Bimap *generateBimap() {
    Bimap *map=(Bimap *)malloc(sizeof(Bimap));
    map->table=(bigram **)calloc(INITIAL_SIZE, sizeof(bigram *));
    map->count=0;
    map->size = INITIAL_SIZE;
    return map;    
}

void freeUnimap(Unimap *map) {
    for (int i = 0; i < map->size; ++i) {
        unigram *current = map->table[i];
        while (current != NULL) {
            unigram *temp = current;
            current = current->next;
            free(temp->w);
            free(temp);
        }
    }
    free(map->table);
    free(map);
}

void freeBimap(Bimap *map) {
    for (int i=0;i<map->size;++i) {
        bigram *current=map->table[i];
        while (current!=NULL) {
            bigram *temp=current;
            current = current->next;
            free(temp->p);
            free(temp);
        }
    }
    free(map->table);
    free(map);
}

void uniDisplay(Unimap *map) {
    printf("\n\nThe UNIGRAM counts in the format\nWORD: COUNT\n");
    for (int i = 0; i < map->size; i++) {
        unigram *current = map->table[i];
        while (current != NULL) {
            printf("%s: %d\n", current->w, current->count);
            current = current->next;
        }
    }
}

void biDisplay(Bimap *map) {
    printf("\n\nThe BIGRAM counts in the format\nWORD-1 WORD-2: COUNT\n");
    for (int i=0;i<map->size;++i) {
        bigram *current=map->table[i];
        while (current!=NULL) {
            printf("%s: %d\n", current->p, current->count);
            current=current->next;
        }
    }
}

void fileDisplay(char **arr, int count) {
    printf("\n");
    for (int i=0;i<count;++i) {
        printf("%s",arr[i]);
    }
    printf("\n");
}


void unigramUpdate(Unimap *map, char **arr, int count) {
    char *word = (char *)malloc(51);
    for (int i = 0; i < count; i++) {
        char *line = arr[i];
        while (*line) {
            while (*line == ' ') {
                line++;
            }
            if (*line == '\0' || *line == '\n') {
                break; 
            }
            char *p = word; 
            while (*line != ' ' && *line != '\0' && *line != '\n') {
                if (isalpha((unsigned char)*line)) { 
                    *p++ = *line++; 
                } else {
                    line++; 
                }
            }
            *p = '\0'; 
            if (strlen(word) > 0) {
                char *p=word;
                for (int i=0;i<strlen(word);++i) {
                    word[i]=tolower(word[i]);
                }
                addUniCount(map, word);
            }
        }
    }
    free(word); 
}

void bigramUpdate(Bimap *map, char **arr, int count) {
    char *phrase=(char *)malloc(103);
    char *word1=(char *)malloc(51);
    for (int i=0;i<count;++i) {
        char *line=arr[i];
        while (*line==' ') {
            line++;
        }
        if (*line == '\0' || *line == '\n') {
                break; 
        }
        char *wrd1p=word1;
        while (*line != ' ' && *line != '\0' && *line != '\n') {
            if (isalpha((unsigned char)*line)) {
                *wrd1p++ =*line;
            }
            line++;
        }
        *wrd1p='\0';
        for (int i=0;i<strlen(word1);++i) {
            word1[i]=tolower(word1[i]);
        }
        while (*line) {
            char *word2=(char *)malloc(51);
            while (*line==' ') {
                line++;
            }
            if (*line=='\0' || *line=='\n') {
                break;
            }
            char *wrd2p=word2;
            while (*line != ' ' && *line != '\0' && *line != '\n') {
                if (isalpha((unsigned char)*line)) {
                    *wrd2p++ =*line;
                }
                line++;
            }
            *wrd2p = '\0';
            for (int i=0;i<strlen(word2);++i) {
                word2[i]=tolower(word2[i]);
            }
            char *ph=phrase;
            if (strlen(word1)> 0 && strlen(word2) > 0) {
                strcpy(ph,word1);  
                strcat(ph," ");
                strcat(ph,word2);
                addBiCount(map, ph);
            }
            word1=strdup(word2);
            free(word2);
        }
    }
    free(word1); 
    free(phrase);
}

char** getSentences(FILE *stream, int *count) {
    char *buffer = (char *)malloc(501 * sizeof(char));
    *count = 0; 
    while (fgets(buffer, 500, stream) != NULL) {
        (*count)++;
    }
    rewind(stream);
    char **arr = (char **)malloc(*count * sizeof(char *));
    for (int i = 0; i < *count; i++) {
        arr[i] = (char *)malloc(501 * sizeof(char));
        fgets(arr[i], 500, stream);
    }
    free(buffer);
    return arr;
}

int main() {
    int ch,count = 0;
    FILE *f = fopen("file.txt", "r");
    if (f == NULL) {
        perror("Failed to open file");
        exit(0);
    }
    char **sentences = getSentences(f, &count);
    Unimap *UNIGRAM = generateUnimap();
    Bimap *BIGRAM=generateBimap();
    printf("Welcome to the program!\n");
    while (1) {
        printf("\nChoose an option");
        printf("\n1. Update the Unigram with new text");
        printf("\n2. Update the Bigram with new text");
        printf("\n3. Display the Unigram content");
        printf("\n4. Display the Bigram content");
        printf("\n5. Display the file content");
        printf("\n6. Exit\n");
        scanf("%d",&ch);
        if (ch==1) {
            unigramUpdate(UNIGRAM,sentences,count); 
            }
        else if (ch==2) {
            bigramUpdate(BIGRAM,sentences,count); 
        }
        else if (ch==3) {
            uniDisplay(UNIGRAM);
        }
        else if (ch==4) {
            biDisplay(BIGRAM); 
        }
        else if (ch==5) {
            fileDisplay(sentences,count); 
        }
        else if (ch==6) {
            freeUnimap(UNIGRAM); 
            freeBimap(BIGRAM); 
            printf("Thank you for using the program!\n"); 
            break;
        }
        else {
            printf("Please choose from the options provided!\n");
        }
    }
    for (int i = 0; i < count; i++) {
        free(sentences[i]);
    }
    free(sentences);
    fclose(f);
    return 0;
}