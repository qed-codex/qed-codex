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

# Informalization of Solution.lean: how the five statements are tied to the theorems of the folder Paper

**This file gives a proof of a few lines for each of the five theorems that `Challenge.lean` states. Each rests on one theorem from the folder `Paper`, which by its comment states the matching result of the paper, in the definitions of the proof. What this file adds is translation: from the definitions of `Statement.lean` to those of the proof, and from "characteristic zero or a prime" to "every natural number $p$". The mathematics is in the files it imports.**

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file has 55 lines. It imports `Statement.lean` and the module `Paper.Approximate`. [Lines 6–7](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L6-L7) Its header says that it proves each statement from the theorem of the paper with that statement. [Lines 9–11](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L9-L11) It declares two conversions and five theorems. The theorems have the names and types of the five in `Challenge.lean`, and no proof body contains `sorry`. [Lines 19–53](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L19-L53) [Challenge.lean, lines 17–31](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Challenge.lean#L17-L31) They stand in another order than in `Challenge.lean`; this note follows the order of `Challenge.lean`. The project's Comparator configuration names this file as the solution module. [comparator.json, line 3](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/comparator.json#L3)

## Two sets of definitions

`Statement.lean` defines circuits, the two polynomials and the classes for the reader. The proof has its own definitions of the same things.

- Circuit size: `Nc.Computes`, written the same way, with the condition on one entry of the list split off as `IsStep`. [Nc/LowDegree.lean, lines 24–31](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/LowDegree.lean#L24-L31)
- Approximating circuits and the Hamiltonian cycle polynomial: `Nc.Approximates` and `Nc.genHC`, written the same way. [Nc/Rate/Defs.lean, lines 24–34](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Rate/Defs.lean#L24-L34)
- The permanent: `Nc.genPerm`, defined as Mathlib's permanent of the matrix of variables, where `Statement.lean` writes the sum out. [Nc/PermValiant.lean, lines 59–61](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/PermValiant.lean#L59-L61)
- Families, VP and VNP: `Nc.Family`, `Nc.VP` and `Nc.VNP`, written the same way up to names. `Nc.VNP` uses a helper, `bits`, for the substitution that `Statement.lean` writes in place. [Nc/Final/CClasses.lean, lines 22–51](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Final/CClasses.lean#L22-L51) The closure of VP: `Paper.VPBar`, written the same way. [Paper/Approximate.lean, lines 20–23](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Approximate.lean#L20-L23)
- The bound: the proof has no name for it. The theorems of `Paper` write the inequality out, where `Statement.lean` has `Beyond`.

For polynomials, circuit sizes and the bound no conversion appears in this file. In line 30 a fact about `Nc.genHC`, `Nc.genPerm`, `Nc.Computes` and the inequality written out is used directly where the goal speaks of `hc`, `perm`, `Computes` and `Beyond`. Lines 43 and 53 do the same. [Line 30](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L30) [Line 43](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L43) [Line 53](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L53) When the project is built, Lean has to see the two sides as equal by unfolding definitions. That includes the permanent, the one pair that is not written the same way. For families a conversion is needed, because the statement and the proof each have a structure of their own. The file defines `toNc` and `ofNc`, which carry the three fields of one structure to the other. [Lines 19–23](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L19-L23)

## Statement 1: the lower bound

`mainTheorem` rests on `Paper.thm_allfields`. [Lines 25–31](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L25-L31) That theorem has the form of `MainTheorem`, but only for $p$ equal to $0$ or a prime. [Paper/Fields.lean, lines 80–86](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Fields.lean#L80-L86) The proof here takes its constant $c$ and splits on $p$.

- If $p$ is $0$ or a prime, the paper theorem gives $m_0$ and the bound.
- Otherwise it takes $m_0 = 0$. There is nothing to prove, because the characteristic of a field is $0$ or a prime.

The statement does not show the value of $c$. The proof of `Paper.thm_allfields` begins by choosing $c = 1/1600^2$. [Paper/Fields.lean, line 87](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Fields.lean#L87)

## Statement 2: the lower bound for approximating circuits

`mainTheoremApprox` rests on the first half of `Paper.thm_approx`, with the same split on $p$. [Lines 38–44](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L38-L44) `Paper.thm_approx` is a conjunction. Its first half is the lower bound for approximating circuits, for $p$ equal to $0$ or a prime. Its second half says that over every field VNP is not contained in the closure of VP. [Paper/Approximate.lean, lines 266–272](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Approximate.lean#L266-L272)

## Statement 3: VP is a proper subset of VNP

`separation` rests on `Paper.cor_allclasses`, which says the same for the classes of the proof. [Lines 33–36](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L33-L36) [Paper/Fields.lean, lines 141–142](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Fields.lean#L141-L142) A proper subset has two halves, and the proof gives both.

- **Inclusion.** For a family $f$ in VP, the proof passes to `toNc f`, applies the inclusion of the proof's classes, and reads the result as $f \in \mathrm{VNP}$.
- **No reverse inclusion.** Suppose VNP were contained in VP in the sense of `Statement.lean`. For a family $g$ in the proof's VNP, apply this to `ofNc g`. That gives the proof's VNP inside the proof's VP, which the second half of `Paper.cor_allclasses` excludes.

## Statement 4: VNP is not contained in the closure of VP

`separationClosure` rests on the second half of `Paper.thm_approx`, with `ofNc` used as in statement 3. [Lines 46–48](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L46-L48)

## Statement 5: the permanent over the real numbers

The proof of `permanent_over_real` is the term `Paper.thm_main`. [Lines 50–53](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Solution.lean#L50-L53) That theorem is stated with `Nc.Computes`, with the sum of the permanent written out and with the inequality written out, so the same unfolding is needed here. [Paper/Rate.lean, lines 527–531](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Rate.lean#L527-L531)

## What this file does not show

- **The mathematics.** None of the argument is in this file. It is in the folder `Paper` and in what that folder imports. Through its two imports this file reaches 320 of the 324 Lean files of the project, `Statement.lean` among them.
- **That the theorems in `Paper` say what the paper says.** Their comments give, in quotation marks, what they present as the paper's statements. [Paper/Fields.lean, lines 80–82](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Fields.lean#L80-L82) [Paper/Fields.lean, line 141](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Fields.lean#L141) [Paper/Approximate.lean, lines 266–267](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Approximate.lean#L266-L267) [Paper/Rate.lean, lines 527–528](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Rate.lean#L527-L528) The README says that an appendix of the paper lists the Lean counterparts of its numbered statements and says where they differ. [README, line 15](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/README.md?plain=1#L15)
- **That the build succeeds.** The README gives the commands and says that the last one should name no axiom other than `propext`, `Classical.choice` and `Quot.sound`. [README, lines 17–23](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/README.md?plain=1#L17-L23) I have not run them.
- **Review by people.** The README says that no human mathematician has checked the proof. [README, line 5](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/README.md?plain=1#L5)

## What I read

I read this file in full. Of the four theorems of `Paper` that it uses I read the statements and their comments, and the first line of the proof of `Paper.thm_allfields`. I did not read the rest of their proofs. I read the proof's definitions listed above. I read `Challenge.lean`, `Statement.lean`, the Comparator configuration and the README. All of this is at the linked revision. I counted the Lean files of the project and followed the import lines from this file. I did not read the paper, and I did not build the project.
