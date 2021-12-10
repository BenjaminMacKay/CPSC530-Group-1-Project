using System;
using System.IO;
using System.Threading.Tasks;

public static class Logic
{
	//Encodes the three possible hands in a game of RPS
	public enum RPS
	{
		Rock, Paper, Scissors
	}

	/** checkWin: Determines whether player won game of RPS
	 *  int player, computer: 0=Rock, 1=Paper, 2=Scissors
	 *  outputs win: 1=player win, 0=computer win
	 */
	public static int CheckWin(int player, int computer)
	{
		int win = Math.Abs(computer - player) switch
		{
			0 => 2,
			1 when player > computer => 1,
			1 when player < computer => 0,
			_ when player > computer => 0,
			_ when player < computer => 1,
		};
		return win;
	}

	//Generates a random RPS hand utilizing simple PRNG 
	public static int CPUPlay()
    {
		Random rand = new Random();

		return rand.Next() % 3;
    }

	/** Write: Writes a line of data to 'data.txt'
	 *  int pl: The hand used by the player
	 *  int win: The outcome of the game
	 *  long time: The time taken in a single game, stored in ticks
	 */
	public static void Write(int pl, int win, long time)
    {
		String output = pl + " " + win + " " + time + "\n";
		using StreamWriter file = new("data.txt", append: true);
		file.Write(output);
		file.Close();
	}

	/** ReadandOutput: A hastily written function that will take in all data contained in 'fn' and print a string to console according to the odd-even algorithm
	 *  string fn: The name of a txt file containing data formatted by write(), value will typically be 'data.txt'
	 *  
	 *  NOTE: This function will crash the program if 'fn' does not exist, error handling was not deemed necessary
	 *        as the three members of this group will never use this function unless 'fn' exists
	 */
	public static void ReadandOutput(string fn)
    {
		string line, output = "";
		StreamReader sr = new StreamReader(fn);
		while((line = sr.ReadLine()) != null)
		{
			string[] parts = line.Split(' ');
			int pl = int.Parse(parts[0]);
			int win = int.Parse(parts[1]);
			int time = int.Parse(parts[2]);

			output += Algo(pl, win, time);
        }
		Console.WriteLine("\nBinary String: \n"+output + "\n");
		sr.Close();
    }

	/** Algo: Performs the simple process of adding pl, win, and time together, and then determining if the resulting value is even or odd
	 *  int pl: The hand chosen by the player
	 *  int win: The result of the game
	 *  int time: The time taken for a single game
	 *  Outputs x: The result of the above described algorithm
	 */
	public static string Algo(int pl, int win, int time)
	{
		string x = ((pl + win + time) & 1) switch
		{
			0 => "0",
			1 => "1"
		};
		return x;
	}

	//When run as main this program will allow the user to play a simple game of RPS against a pseudo-random opponent,
	//at any time the option '4' can be used to produce a binary string based off of Algo().
	//The program must be manually exited, otherwise it will loop continuously.
	static void Main()
	{
		String input;
		while (true)
		{
			long start = DateTime.Now.Ticks;
			Console.WriteLine("Enter option for player (Rock=0, Paper=1, Scissors=2, Output current binary string=4)");

            while (true)
            {
				input = Console.ReadLine();
				if (input == "0" || input == "1" || input == "2" || input == "4") break;
				Console.WriteLine("Please provide a valid input.");
			}

			if(input != "4")
			{
				int pl = int.Parse(input);

				int cpu = CPUPlay();
				Console.WriteLine("You Played: " + (RPS)pl);
				Console.WriteLine("Computer played: " + (RPS)cpu);

				int win = CheckWin(pl, cpu);
				Console.WriteLine("Result (1 = Player win, 0 = CPU win, 2 = Tie): " + win);
				Console.WriteLine("\n");


				long time = DateTime.Now.Ticks - start;
				Console.WriteLine("Played: " + pl + ", Win/Loss: " + win + ", Time taken: " + time);
				Console.WriteLine("\n");

				Write(pl, win, time);

			}else ReadandOutput("data.txt");

		}
	}
}
