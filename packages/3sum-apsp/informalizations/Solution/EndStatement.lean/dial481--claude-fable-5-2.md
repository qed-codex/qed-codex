---
{
  "module": "Solution/EndStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# Informalization of Solution/EndStatement.lean: a file that only imports the five proofs

**This file has nine lines and declares nothing. It imports one module of the library, `ThreeSumApsp.Statements.EndStatement`, in which the five theorems of `Challenge/EndStatement.lean` are proved under the same names. To see how the five claims are obtained one has to read that module, so this note describes it as well. There each claim is one of the bounds of an item of the paper, which the library states as a theorem elsewhere, put into the form of the end statement.**

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

After the licence header the file has one import and one comment. [Lines 6–9](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Solution/EndStatement.lean#L6-L9) The comment says that this file imports the theorems that have the names of the statements of `Challenge/EndStatement.lean` and adds nothing of its own. [Lines 8–9](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Solution/EndStatement.lean#L8-L9) A Comparator configuration of the project names this file as the solution module for the five theorems. [comparator-endstatement.json, lines 1–18](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/comparator-endstatement.json#L1-L18)

## The imported module

`ThreeSumApsp/Statements/EndStatement.lean` has 68 lines. It imports three modules of the library. [Statements/EndStatement.lean, lines 8–10](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean#L8-L10) It has five theorems with the names and types of the five in the challenge file. None contains `sorry` in its own text. [Statements/EndStatement.lean, lines 36–66](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean#L36-L66) [Challenge/EndStatement.lean, lines 56–80](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/EndStatement.lean#L56-L80)

Its header explains the plan. The library has item statements for the paper's Theorems 19 and 22 and Corollary 39. They speak of the problems of the end statement and contain the five bounds, with real exponents. The three used here are `Items.Theorem_19`, `Items.Theorem_22_second` and `Items.Corollary_39_zero`. A lemma, `SolvedInTime.endStatement`, turns a bound in the library's own notion of solving, which has a real exponent, into the form of the end statement: the same program and the same $b$, a step bound with natural numbers as values, and a rational exponent. [Statements/EndStatement.lean, lines 12–18](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean#L12-L18) [Exponents.lean, lines 67–70](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/Exponents.lean#L67-L70)

## The five proofs

Each proof applies `SolvedInTime.endStatement` to one bound and checks two conditions on the exponent by calculation: that the rational exponent equals the real one, and that it is not negative.

1. **Exact Triangle.** The bound is the third of the three bounds of `Items.Theorem_19`. [Statements/EndStatement.lean, lines 36–40](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean#L36-L40) [RunningTimes/Sec3/Theorem19.lean, lines 67–76](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem19.lean#L67-L76) The header says that this bound follows from the second and so rests on the paper's Corollary 26, and not on the time bound of Theorem 5. [Statements/EndStatement.lean, lines 22–24](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean#L22-L24)
2. **3SUM, the (min,+)-product and shortest paths.** The three bounds are the first, the fourth and the fifth of the five bounds of `Items.Theorem_22_second`. The theorem that proves this item, `wordRam_theorem_22_second`, has the comment "the bounds using Corollary 26". [Statements/EndStatement.lean, lines 42–55](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean#L42-L55) [RunningTimes/Sec3/Theorem22.lean, lines 107–128](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec3/Theorem22.lean#L107-L128)
3. **Zero-Weight $k$-Clique.** For $k \ge 3$ the bound comes from the theorem `wordRam_corollary_39_zero`. Here the exponent $k - 0.0017 \lfloor k/3 \rfloor$ depends on $k$, and the proof shows that it is not negative from $\lfloor k/3 \rfloor \le k$ and $k \ge 0$. [Statements/EndStatement.lean, lines 57–66](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean#L57-L66) [RunningTimes/Sec5/Corollary39.lean, lines 32–34](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/RunningTimes/Sec5/Corollary39.lean#L32-L34)

According to the header, all five claims go back to one route of the paper, the one through its Corollary 26. [Statements/EndStatement.lean, lines 20–27](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Statements/EndStatement.lean#L20-L27)

## What this file does not show

- **The mathematics and the programs.** They are in the library, the folder `ThreeSumApsp`. The project has 434 Lean files, 426 of them in that folder.
- **What the item statements say in full.** `Items.Theorem_19`, `Items.Theorem_22_second` and `Items.Corollary_39_zero` are defined in the root file `PaperStatements.lean`, which has 4,194 lines. [PaperStatements.lean, lines 3884–3887](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/PaperStatements.lean#L3884-L3887) [PaperStatements.lean, lines 3905–3910](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/PaperStatements.lean#L3905-L3910) [PaperStatements.lean, lines 4065–4067](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/PaperStatements.lean#L4065-L4067) Of that file I read only these three definitions and the definition of the library's notion of solving.
- **That the build succeeds.** I have not built the project and have not run Comparator.

## What I read

I read this file and `ThreeSumApsp/Statements/EndStatement.lean` in full. I read the statements and comments of `SolvedInTime.endStatement`, `wordRam_theorem_19`, its third bound, `wordRam_theorem_22_second` and `wordRam_corollary_39_zero`, not their proofs. I read `Challenge/EndStatement.lean`, the root file `EndStatement.lean`, the three item definitions named above and the Comparator configuration. All of this is at the linked revision. I counted the Lean files of the project and the lines of the root file `PaperStatements.lean`. I did not read the paper, and I did not build the project.
