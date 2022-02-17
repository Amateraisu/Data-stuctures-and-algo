

int mostWordsFound(char ** sentences, int sentencesSize){
    //Max number of words found in sentences can be done 
    //by calculating the number of space characters
    char* ptr ;
    int word_Counter = 0;
    int index = 0;
    int max = 0;
    
    
    for (int i =0; i < sentencesSize ; i++)
    {
        word_Counter = 0;
        index = 0;
        ptr = sentences[i];
        while (ptr[index] != '\0')
        {
            if (ptr[index] == ' ')
            {
                word_Counter++;
            }
            index++;
        }
        if (word_Counter > max)
        {
            max = word_Counter;
        }
    }
    

    
    
    return max + 1;
}