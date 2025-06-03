from database.DB_connect import DBConnect
from model.team import Team


class DAO():
    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = '''select DISTINCT t.`year` 
                    from teams t 
                    where t.`year` >= 1980 
                    ORDER by t.`year` DESC'''

        cursor.execute(query)
        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getTeamsByYear(year):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = '''SELECT *
                    from teams t 
                    where t.`year` = %s'''

        cursor.execute(query, (year,))
        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSalyOfTeams(year, idMap):
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)

        query = '''SELECT t.teamCode, t.ID, sum(s.salary) as totSalary
                    from salaries s, teams t, appearances a 
                    WHERE s.`year`= t.`year` and t.`year` = a.`year`
                    and s.`year` = %s
                    and t.ID = a.teamID 
                    GROUP by t.teamCode'''

        cursor.execute(query, (year,))
        for row in cursor:
            #result.append(idMap[row["ID"]], row["totSalary"])
            result[idMap[row["ID"]]] = row["totSalary"]

        cursor.close()
        conn.close()
        return result

