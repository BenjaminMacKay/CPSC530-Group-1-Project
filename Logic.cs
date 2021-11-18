using System;

public static class Logic
{

	/** checkWin: Determines whether player won game of RPS
	 *  int player, computer: 0=Rock, 1=Paper, 2=Scissors
	 *  outputs win: 1=player win, 0=computer win
	 */
	public static int CheckWin(int player, int computer)
	{
		int win = Math.Abs(computer - player) switch
		{
			0 => 0,
			1 when player > computer => 1,
			1 when player < computer => 0,
			_ when player > computer => 0,
			_ when player < computer => 1,
		};
		return win;
	}

	//For testing purposes
	static void Main()
	{
		Console.WriteLine("Enter option for player (Rock=0, Paper=1, Scissors=2)");
		int pl = int.Parse(Console.ReadLine());

		Console.WriteLine("Enter option for computer (Rock=0, Paper=1, Scissors=2)");
		int cpu = int.Parse(Console.ReadLine());

		int win = CheckWin(pl, cpu);
		Console.WriteLine("Result (1 = Player win, 0 = CPU win): " + win);

	}

}
