<?php

$first_program = `python first_program.py`;
echo "<center><h1>First Program</h1></br>";
echo $first_program;
echo "</center><hr>";

$classes_journal = `python classes_journal.py`;
echo "<h1>Classes Journal</h1></br>";
echo $classes_journal;
echo "<hr>";

$S3 = `python S3.py`;
echo $S3;
echo "<hr>";

$S4 = `python S4.py`;
echo $S4;
echo "<hr>";

$S5 = `python S5.py`;
echo $S5;
echo "<hr>";

$S6 = `python S6.py`;
echo $S6;

?>
