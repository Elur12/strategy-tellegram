import config
import sqlManager
import aiogram



if __name__ == "__main__":
    sqlConfig = sqlManager.main()
    users = sqlManager.users(sqlConfig)
    campChange = sqlManager.campChange(sqlConfig)
    timeTable = sqlManager.timeTable(sqlConfig)
    personalHistory = sqlManager.personalHistory(sqlConfig)
    commandHistory = sqlManager.commandHistory(sqlConfig)
    causePersonal = sqlManager.causePersonal(sqlConfig)
    causeCommand = sqlManager.causeCommand(sqlConfig)
    achievements = sqlManager.achievements(sqlConfig)
    