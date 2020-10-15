public class Vigenere
{
    public static void main(String[] args)
    {
        //Have a for loop that starts at 3 characters with an string and int array (without defined parts)
        //Run through the entire code, keeping track of each string that is recorded and how many  times it appears
        // --Should keep track of distance between them
        //Have the for loop continue on with 4 characters etc after printing the information. 
        //After the information is printed, it's possible to exit out of the program and modify it so that it checks for the distance for that string

        String input = args[0];

        // Mr. K came in and said that we find the repeats ourselves and not with code
        // Write code that loops through for a given text segment, and just counts the distance between each occurance

        String target = args[1];
        int len = target.length(); //he gave hint that keylength is 4
        int repeats = 0;
        int sincelastrepeat = -999;

        for (int i=0; i < input.length(); i+= len)
        {
            if (input.substring(i,i+len).equals(target))
            {
                repeats++;
                sincelastrepeat=0;
            }

        }

    }

}