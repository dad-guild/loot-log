A repository for tracking loot council assignments within Dad Guild (Benediction).

* `discord/`
  * user-readable logs exported from Gargul for posting in Discord
  * the format string used is `@WINNER - @ITEM (@ID) @ROLLTYPE @DATE @TIME`
* `csv/`
  * CSV files for import into TMB
  * the CSVs are deterministically generated from files in `discord/`
* `legacy/`
  * older loot logs from before TMB was involved
* `convert.py`
  * converts a loot log (of the format used in the `discord/` directory) to a CSV file
* `regenerate.bash`
  * run this after modifying anything in the `discord/` directory
  * sorts all the files in `discord/` and regenerates the corresponding CSV files
  * files are sorted to make diffs easier to read since gargul export does not appear to have deterministic ordering

