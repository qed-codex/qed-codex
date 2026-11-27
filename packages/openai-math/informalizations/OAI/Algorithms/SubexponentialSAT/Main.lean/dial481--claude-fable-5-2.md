---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# Informalization of OAI/Algorithms/SubexponentialSAT/Main.lean: a file that imports the proof and names two theorems

**This file has sixteen lines and declares nothing. It imports two modules and, in a comment, names two theorems of the library: the main theorem of a manuscript on bounded-width SAT, and `exact_count_and_sat`, the theorem that the challenge file states. The second is proved in one of the two imported modules, `SqrtLogSpace/Final.lean`. To see how the challenge statement is obtained one has to read that module, so this note describes it as well.**

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file has two imports, `SqrtLog.ExecutionNativeFinal` and `SqrtLogSpace.Final`, a namespace and one comment. [Lines 1–16](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Main.lean#L1-L16) The comment says two things. A theorem called `SubexponentialSAT.SubexpOrderedRawMainTheorem.mainTheorem_explicit` is the formalized main theorem of a manuscript, "A Subexponential Algorithm for Bounded-Width SAT". And `SubexponentialSAT.SqrtLogSpace.exact_count_and_sat` strengthens a later result, which the comment calls the square-root-logarithmic result, with exact counting and a polynomial bound on the visited tape space. [Lines 6–14](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Main.lean#L6-L14)

A Comparator configuration names this file as the solution module for the one theorem `exact_count_and_sat`. [SubexponentialSAT.json, lines 3–6](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.json#L3-L6) So the file's task is to make that theorem available by its imports.

## The module with the theorem

`SqrtLogSpace/Final.lean` has 201 lines and five theorems. [SqrtLogSpace/Final.lean, lines 1–201](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L1-L201)

**The compiled form.** `compiled_exact_count_and_sat` has the conclusion of the challenge statement for one particular kind of machine. For every $k \ge 2$ it gives a program of type `BitProgram.Program 80 1220 labels` with `program.outputStack = 1216`. The machine is `GuardedCompiler.primitive program`. Both names come from modules that I did not read. I read the second as a compiler from programs to machines. The tapes of the machine are indexed by `Fin 1220`, so there are 1220 of them. The count is on tape 256 and the answer on tape 1216. [SqrtLogSpace/Final.lean, lines 10–34](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L10-L34)

Its proof takes a cutoff and constants from `NativeLargeEntry.run`. It enlarges the constants once, so that one set serves all $n$: it adds $28700$ to $C$, $1$ to $A$, $5022741$ to $S$ and $2$ to each of $d$ and $e$. Two lemmas, `NativeOuterBudgets.runtime_with_fallback` and `NativeOuterBudgets.space_with_fallback`, are used for this step. The program is `Native.countingProgram cutoff k (NativeLeafProgram.command k)`, so it depends on the cutoff. Then the proof splits on the number of variables. For $n$ up to the cutoff it uses `Native.entry_small_primitive`. For larger $n$ it uses the result that came with the cutoff. [SqrtLogSpace/Final.lean, lines 35–69](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L35-L69)

**The challenge statement.** The statement of `exact_count_and_sat` has the same text as the statement in the challenge file. I compared lines 71 to 97 here with lines 191 to 217 there, and they are equal. Its proof takes the program from the compiled form, names the compiled machine and the two tapes, and passes the rest on unchanged. [SqrtLogSpace/Final.lean, lines 71–102](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L71-L102) [ComparatorChallenges/SubexponentialSAT.lean, lines 191–218](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L191-L218)

**Three more theorems.** The module derives three further statements from the compiled form. They are not in the Comparator configuration.

- `exact_count_eth` is a variant for $n \ge 20$ with new constants. Both bounds are written in $n$ plus the number of clauses plus $1$, in place of the length of the input. The time bound uses a scale called `rho`, which is defined in a module that I did not read. [SqrtLogSpace/Final.lean, lines 104–147](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L104-L147)
- `sat_polynomial_space` is a statement for $k \ge 3$ with the same form of machine and the same two bounds. It adds a Boolean `answer` that is true exactly when $F$ is satisfiable. [SqrtLogSpace/Final.lean, lines 149–182](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L149-L182)
- `original_sat_main` proves a proposition called `SqrtLog.Statement.MainTheorem` from `sat_polynomial_space`. [SqrtLogSpace/Final.lean, lines 184–193](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L184-L193)

The module ends with five commands that print the axioms on which these five theorems depend. [SqrtLogSpace/Final.lean, lines 197–201](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L197-L201)

## What this file does not show

- **The mathematics.** None of the argument is in this file, and little of it is in `SqrtLogSpace/Final.lean`. That module refers to `NativeLargeEntry.run`, `Native.entry_small_primitive`, `Native.countingProgram` and the two `NativeOuterBudgets` lemmas. I did not read where these are defined, and I did not check the modules behind them for `sorry` or for the axioms they use. The folder `OAI/Algorithms/SubexponentialSAT` has 3,977 files at this revision.
- **That the statement means the same.** The text of the statement equals that of the challenge. But `SqrtLogSpace/Final.lean` does not import the challenge file. [SqrtLogSpace/Final.lean, lines 1–3](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L1-L3) Its names, such as `SAT.CNF`, `Encoding.encodeCNF`, `LocatedCfg` and `visitedSpace`, refer to definitions of the library in modules that I did not read. To check that these agree with the definitions of the challenge is the task of a Comparator run, and I have not run one.
- **The first theorem named in the comment.** `mainTheorem_explicit` is not used in the proof described above, as far as `SqrtLogSpace/Final.lean` shows. I did not look for it.
- **The Exponential Time Hypothesis.** Neither this file nor `SqrtLogSpace/Final.lean` states it. One of the three further theorems has "eth" in its name, and the header of that module speaks of an "ETH square-root-log time scale". [SqrtLogSpace/Final.lean, lines 5–6](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean#L5-L6)
- **That the build succeeds.** I have not built the project and have not run Comparator. The configuration sets `enable_nanoda` to `false`. [SubexponentialSAT.json, line 13](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.json#L13) In Comparator, setting that switch to `true` adds a check with a second kernel, nanoda, to the check with Lean's own kernel. [Comparator README, lines 12–13](https://github.com/leanprover/comparator/blob/865edc14486c3388e9225daa971da8e157488c3e/README.md?plain=1#L12-L13) [Comparator README, lines 86–87](https://github.com/leanprover/comparator/blob/865edc14486c3388e9225daa971da8e157488c3e/README.md?plain=1#L86-L87)

## What I read

I read this file, `SqrtLogSpace/Final.lean`, the challenge file and its Comparator configuration in full, at the linked revision. I read the lines of the Comparator README that describe the second kernel. I counted the files of the folder from the repository's file list. I did not read any other module of the library. I did not read the manuscript, and I did not build the project.
