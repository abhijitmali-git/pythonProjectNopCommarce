pytest -v -s -m "sanity" --html=Reports\reports.html TestCases/ --browser Chrome
REM pytest -v -s -m "sanity and regression" --html=Reports\reports.html TestCases/ --browser Chrome
REM pytest -v -s -m "sanity or regression" --html=Reports\reports.html TestCases/ --browser Chrome
REM pytest -v -s -m "regression" --html=Reports\reports.html TestCases/ --browser Chrome



REM pytest -v -s -m "sanity" --html=Reports\reports.html TestCases/ --browser Firefox
REM pytest -v -s -m "sanity and regression" --html=Reports\reports.html TestCases/ --browser Firefox
REM pytest -v -s -m "sanity or regression" --html=Reports\reports.html TestCases/ --browser Firefox
REM pytest -v -s -m "regression" --html=Reports\reports.html TestCases/ --browser Firefox