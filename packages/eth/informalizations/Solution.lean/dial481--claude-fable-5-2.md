---
{
  "module": "Solution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# Informalization of Solution.lean: where the two theorems are proved

**This file gives a one-line proof term for each of the two theorems that `Challenge.lean` states. The Main Theorem is a theorem from another file under a new name. The failure of the Exponential Time Hypothesis is obtained from it by applying two further theorems in turn and taking one part of the result. The mathematics is in the files these three theorems come from. This file only joins them.**

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file has 44 lines. It imports `MainResults.lean`, which holds the two statements, and three modules of the proof: `CountedRoute.Main`, `NamesInOrder.Main` and `Wrap.Main`. [Lines 6–9](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L6-L9) It declares two theorems with the names and types of the two in `Challenge.lean`: `MainResults.ethIsFalse` of type `MainResults.ETHIsFalse` and `MainResults.mainTheorem` of type `MainResults.MainTheorem`. Neither body is `sorry`. [Line 40](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L40) [Line 44](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L44) [Challenge.lean, lines 12–17](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean#L12-L17) The project's Comparator configuration names this file as the solution module. [comparator.json, line 3](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/comparator.json#L3)

## The Main Theorem

`MainResults.mainTheorem` is proved by the term `CountedRoute.mainTheoremHolds`. [Lines 42–44](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L42-L44) That theorem has the type `CountedRoute.MainTheoremHolds`, which is defined as the proposition `MainTheoremAllOccur`. [CountedRoute/Main.lean, lines 91–92](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/CountedRoute/Main.lean#L91-L92) [CountedRoute/Defs.lean, lines 139–141](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/CountedRoute/Defs.lean#L139-L141)

`MainTheoremAllOccur` is stated in a file of the proof. It is written with the hypotheses of `MainResults.MainTheorem` in the same order: one machine with finite alphabets and one constant $C$, for every $k \ge 1$ and every $k$-CNF with $m \ge 2$ clauses over $n \ge 4$ variables that all occur. It uses the proof's own definitions of these notions, which I did not read. [MainTheoremFormsStatement.lean, lines 107–122](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/MainTheoremFormsStatement.lean#L107-L122) The header of this file says that `MainResults.MainTheorem` unfolds to it, and that Lean accepts the one-line proof by unfolding definitions. [Lines 21–22](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L21-L22) So the proof works with its own copy of the statement. When the project is built, line 44 is where Lean has to accept that the copy and the statement of `MainResults.lean` agree after unfolding definitions.

The header also says how `CountedRoute.mainTheoremHolds` is obtained. It comes from the chain of statements in `proof/maintheorem/CountedRoute`. The header says that this chain follows the order of the paper's proof, with differences that are listed at the head of the index of the paper's statements, and that it starts from the machine of the paper's Theorem A (b). [Lines 13–17](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L13-L17)

## The Exponential Time Hypothesis

The proof is the term `(Wrap.countingBoundImpliesFailureOfETH (NamesInOrder.generalFormFollowsAsPropositions CountedRoute.mainTheoremHolds)).2.2.1`. [Line 40](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L40) It reads from the inside out.

1. `CountedRoute.mainTheoremHolds` is the Main Theorem in the form `MainTheoremAllOccur`, where every variable occurs.
2. `NamesInOrder.generalFormFollowsAsPropositions` is the implication from `MainTheoremAllOccur` to `MainTheoremCompact`. [NamesInOrder/General.lean, lines 60–63](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/General.lean#L60-L63) [NamesInOrder/Defs.lean, lines 221–224](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/Defs.lean#L221-L224) `MainTheoremCompact` is the Main Theorem for formulas over $x_0, \dots, x_{N-1}$ of which $n \ge 4$ occur. The count is over assignments of the $n$ variables that occur. The input uses another code, called the compact code, and the time bound has an added term $C \cdot \ell^C$, where $\ell$ is the length of that code. [MainTheoremFormsStatement.lean, lines 243–251](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/MainTheoremFormsStatement.lean#L243-L251) The header describes the argument as a front end that renames the variables that occur. [Lines 24–26](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L24-L26)
3. `Wrap.countingBoundImpliesFailureOfETH` is the implication from `MainTheoremCompact` to a conjunction of five statements. [Wrap/Main.lean, lines 113–115](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Main.lean#L113-L115) [Wrap/Defs.lean, lines 185–188](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Defs.lean#L185-L188) In the order of the conjunction they are: one machine decides 3-SAT within $c \cdot 2^{\delta n}$ steps for every $\delta > 0$; for every $\delta > 0$ some machine does; the hypothesis $s_3 > 0$ fails; the sentence of the paper's Theorem 2, that for every $\delta > 0$ some algorithm decides 3-SAT in time $O(2^{\delta n})$; and the failure of the hypothesis as the paper defines it, $s_k > 0$ for all $k \ge 3$. [Wrap/Defs.lean, lines 179–183](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Defs.lean#L179-L183) [PaperSentencesStatement.lean, lines 99–111](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/PaperSentencesStatement.lean#L99-L111)
4. `.2.2.1` takes the third of the five, `¬ Sat3.ETH_TM`. `Sat3.ETH_TM` is the proposition $s_3 > 0$ as the proof states it. [ThreeSatStatement.lean, lines 77–79](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ThreeSatStatement.lean#L77-L79) The header says that `¬ Sat3.ETH_TM` unfolds to `MainResults.ETHIsFalse`. [Lines 33–35](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L33-L35)

The first of the five statements says more than `MainResults.ETHIsFalse` asks for. There the same machine serves every $\delta > 0$, and only the constant depends on $\delta$. [ThreeSatRateStatement.lean, lines 87–91](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/ThreeSatRateStatement.lean#L87-L91) The statement of `MainResults.lean` allows a different machine for each $\delta$. This file does not restate the stronger form as a theorem of its own.

In the first implication both sides are theorems. Its comment says so, and adds that by its statement alone the implication shows little and that what an arbitrary machine gives is said by `GeneralFormFollows`. [NamesInOrder/Defs.lean, lines 221–223](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/Defs.lean#L221-L223) The comment on the second implication points in the same way to `CounterCanBeWrappedAndEveryWrapperDecides`. [Wrap/Defs.lean, lines 185–187](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/Defs.lean#L185-L187) The header of this file says that each of the two arguments is proved for every machine that has the bound it starts from. [Lines 23–24](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L23-L24)

## Cost inside the proof and in the statements

The header says that the proof uses notions of cost that differ from the count of steps in the statements. Inside the proof an operation is one query to a table or one step of a machine, and a step may be any computation that takes time polynomial in the size of the machine's state. From the hypothesis of the paper's Theorem D (a) on, cost is measured as the length of a string of blank symbols that is given with the input as a budget of time. [Lines 17–21](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L17-L21)

The header then says why this cannot weaken the result. The types of the two theorems count steps of one of Mathlib's Turing machines, and Lean's kernel checks the proofs against these types. [Lines 29–31](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L29-L31) It adds that inside the proof one operation may cost time polynomial in the bound on the operations, so that an exponent of the paper holds in machine steps only up to a constant factor, which the $O$ in the conclusion of the paper's Theorem D (a) absorbs. [Lines 31–33](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Solution.lean#L31-L33)

## What this file does not show

- **The mathematics.** None of the argument is in this file. It is in the three proof modules this file imports and in what they import. The project has 1,052 Lean files in all.
- **That the build succeeds.** The README gives the commands and the expected output: both theorems depend only on the axioms `propext`, `Classical.choice` and `Quot.sound`. [README, lines 24–39](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/README.md?plain=1#L24-L39) I have not run them.
- **That the statements match the paper.** The README says that no machine checks that `MainResults.lean` says what the paper says. [README, line 22](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/README.md?plain=1#L22)

## What I read

I read this file in full. Of the three theorems it names I read the statements and their comments, not the proofs. I read the definitions of `MainTheoremAllOccur`, `MainTheoremCompact`, `OneMachineEveryDeltaAndETHFails`, `SubexpTM`, `ETH_TM` and the two `PaperSentences` propositions among the five. I read `Challenge.lean`, `MainResults.lean`, the Comparator configuration and the README. All of this is at the linked revision. I counted the Lean files of the project. I did not read the paper, and I did not build the project.
