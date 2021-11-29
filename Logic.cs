using System;
using System.IO;
using System.Threading.Tasks;

public static class Logic
{

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

	public static int CPUPlay()
    {
		Random rand = new Random();

		return rand.Next() % 3;
    }

	public static void Write(int pl, int win, long time)
    {
		String output = pl + " " + win + " " + time + "\n";
		using StreamWriter file = new("data.txt", append: true);
		file.Write(output);
		file.Close();
	}

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

	public static string Algo(int pl, int win, int time)
	{
		string x = ((pl + win + time) & 1) switch
		{
			0 => "0",
			1 => "1"
		};
		return x;
	}

	//For testing purposes
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

				//Console.WriteLine("Enter option for computer (Rock=0, Paper=1, Scissors=2)");
				//int cpu = int.Parse(Console.ReadLine());
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
