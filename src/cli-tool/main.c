#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {

        if (argc < 2) {
                fprintf(stderr, "[ERROR]: To less arguments found!");
                return 1;
        }

        FILE *file = fopen("./main/main.py", "a");

        if (file == NULL) {
                fprintf(stderr, "[ERROR]: No file found. Please check the health of this repo!");
                return 1;
        }

        char *option = argv[1];
        char cmdAdd[256];
        char cmdCompress[256];
        char cmdDeCompress[256];

        snprintf(cmdAdd,        sizeof(cmdAdd),        "mow.addFile('/%s')",      argv[2]);
        snprintf(cmdCompress,   sizeof(cmdCompress),   "mow.combineFiles('%s')",  argv[2]);
        snprintf(cmdDeCompress, sizeof(cmdDeCompress), "mow.separateFiles(%s)",   argv[2]);

        int opt = 0;
        
        if      (strcmp(option, "add")        == 0) opt = 1;
        else if (strcmp(option, "compress")   == 0) opt = 2;
        else if (strcmp(option, "decompress") == 0) opt = 3;

        // cli cmds
        switch (opt) {
                case 1:
                        fputs(cmdAdd, file);
                        fprintf(stdout, "Add: File, $: %s", argv[2]);
                        break;
                case 2:
                        fputs(cmdCompress, file);
                        fprintf(stdout, "Compress: File, $: %s", argv[2]);
                        break;
                case 3:
                        fputs(cmdDeCompress, file);
                        fprintf(stdout, "Decompress: File, $: %s", argv[2]);
                        break;
                default:
                        fprintf(stderr, "[ERROR]: Invalid Cmd, you may want to read the docs! $: %s", argv[2]);
                        break;
        }
        fputs("\n", file);
        fclose(file);
        return 0;
}
