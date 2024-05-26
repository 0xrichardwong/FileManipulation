<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>File Manipulator Script</h1>
    <p>This Python script performs various text file manipulation tasks based on command line arguments. It offers functionalities such as reversing content, copying content, duplicating content, and replacing specific characters within a text file.</p>
    <h2>Usage</h2>
    <p>To use the script, execute it from the command line with the following syntax:</p>
    <pre><code>python script.py [operation] [arguments]</code></pre>
    <p>Where:</p>
    <ul>
        <li><code>[operation]</code> specifies the manipulation operation to perform.</li>
        <li><code>[arguments]</code> are optional and depend on the operation being executed.</li>
    </ul>
    <h2>Operations</h2>
    <ol>
        <li><strong>Reverse:</strong> Reverses the content of the input file and writes the reversed content to the output file.</li>
        <li><strong>Copy:</strong> Copies the content of the input file directly to the output file.</li>
        <li><strong>Duplicate:</strong> Duplicates the content of the input file a specified number of times and writes the duplicated content to the output file. The number of duplications is provided as an argument.</li>
        <li><strong>Replace:</strong> Replaces occurrences of a specified character or substring in the input file with another character or substring. The characters to replace and their replacements are provided as arguments.</li>
    </ol>
    <h2>Example</h2>
    <p>For example, to reverse the content of a file named <code>Input.txt</code> and save the result to <code>Output.txt</code>, execute:</p>
    <pre><code>python script.py reverse</code></pre>
    <p>To duplicate the content of <code>Input.txt</code> three times and save it to <code>Output.txt</code>, execute:</p>
    <pre><code>python script.py duplicate 3</code></pre>
    <p>To replace all occurrences of the character 'a' with 'b' in <code>Input.txt</code> and save the modified content to <code>Output.txt</code>, execute:</p>
    <pre><code>python script.py replace a b</code></pre>
    <h2>Notes</h2>
    <ul>
        <li>Ensure that the input file path is correctly set in the script (<code>inputPath</code> variable).</li>
        <li>Output files will be written to the directory specified by <code>outputPath</code>.</li>
    </ul>
</body>
</html>
