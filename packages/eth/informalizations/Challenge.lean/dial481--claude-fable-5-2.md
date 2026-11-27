---
{
  "module": "Challenge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "license": "CC-BY-4.0"
}
---

# Informalization of Challenge.lean: the Exponential Time Hypothesis is false, and a counting bound for k-CNF formulas

**This file states two theorems and proves neither. The first says that the Exponential Time Hypothesis is false. In the source's reading: for every $\delta > 0$ some deterministic Turing machine decides 3-SAT on $n$ variables within $c \cdot 2^{\delta n}$ steps, for some constant $c$. The second, called the Main Theorem, says that one machine counts the satisfying assignments of every $k$-CNF formula with $k \ge 1$, $m \ge 2$ clauses and $n \ge 4$ variables that all occur, within $2^{C \min\{km/\sqrt{\log m},\ k^2 n \log\log n/\sqrt{\log n}\}}$ steps, with one constant $C$ for every $k$.** Both theorems end in `sorry`. What the statements mean is fixed in a second file, `MainResults.lean`, which this note reads as well.

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file has 17 lines. It imports `MainResults.lean` and nothing else. [Line 6](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean#L6) Its header says that `MainResults.lean` imports Mathlib alone, that a reader of that file knows all that the two statements mean, and that nothing imports this file. [Lines 8–9](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean#L8-L9) `MainResults.lean` says the same of itself: it imports only Mathlib and has definitions only, no theorem and no proof. [MainResults.lean, lines 6–12](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L6-L12)

The two theorems are `MainResults.ethIsFalse` and `MainResults.mainTheorem`. Each has the body `sorry`. [Lines 12–13](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean#L12-L13) [Lines 16–17](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean#L16-L17) The project's Comparator configuration names this file as the challenge and `Solution` as the module that has to prove the same two statements. It permits the axioms `propext`, `Quot.sound` and `Classical.choice`. [comparator.json, lines 1–15](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/comparator.json#L1-L15) I have not built the project and have not run Comparator.

## The machine

An algorithm is a machine of Mathlib's kind `Turing.FinTM2`. It is deterministic and has finitely many stacks in place of tapes. On a stack it can push a symbol, pop the top symbol or read it. Time is the number of steps. One step runs the current block of the program until it jumps to a block or halts. For a fixed machine this is a bounded number of stack operations. [MainResults.lean, lines 23–29](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L23-L29)

Input and output are words of bits. The machine starts with the input on its input stack and all other stacks empty. It has to halt with the output on its output stack, all other stacks empty and its internal state back at the initial value. [MainResults.lean, lines 26–32](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L26-L32) Both statements also require every stack alphabet to be finite. The source says that Mathlib alone requires this only of the input stack. [MainResults.lean, lines 32–34](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L32-L34)

## Formulas and their codes

A literal on $x_0, \dots, x_{n-1}$ is a pair $(i, b)$: the variable $x_i$ if $b$ is true and its negation if $b$ is false. A clause is a list of literals, read as their OR. A formula is a list of clauses, read as their AND. [MainResults.lean, lines 58–62](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L58-L62)

A formula is a $k$-CNF if every clause has at most $k$ literals and no clause is written twice. Clauses are lists. A clause may be empty, and then it is false. It may repeat a literal. The same literals in another order make a different clause. [MainResults.lean, lines 64–69](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L64-L69)

For fixed $k$ the input word is $1^n 0$, followed for each clause by $k$ positions of $\lfloor \log_2 (2n) \rfloor + 1$ bits each, lowest bit first. For $n = 0$ a position has one bit. A position holds $0$ if it is empty, $2i + 1$ for $\neg x_i$ and $2i + 2$ for $x_i$. [MainResults.lean, lines 71–75](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L71-L75) [MainResults.lean, lines 82–87](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L82-L87)

## First statement: the Exponential Time Hypothesis is false

The definitions are built in four steps.

1. A machine decides $k$-SAT within $t(n)$ steps if the following holds for every $n$ and every $k$-CNF $\varphi$ on $x_0, \dots, x_{n-1}$. Started on the code of $\varphi$, it halts after at most $t(n)$ steps with one bit, and that bit is $1$ exactly when $\varphi$ is satisfiable. No bound on the number of clauses is assumed, and $k$ is not part of the input. [MainResults.lean, lines 89–95](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L89-L95) Since no clause is written twice, a $k$-CNF on $n$ variables has at most $(2n+1)^k$ clauses. [MainResults.lean, lines 66–67](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L66-L67)
2. `InTime k δ` says that there are a machine with finite alphabets and a constant $c$ such that the machine decides $k$-SAT within $\lfloor c \cdot 2^{\delta n} \rfloor$ steps. The machine and $c$ may depend on $k$ and on $\delta$. [MainResults.lean, lines 97–102](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L97-L102)
3. $s_k$ is the infimum of all $\delta \ge 0$ for which `InTime k δ` holds. It is a number in $[0, \infty]$. [MainResults.lean, lines 104–107](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L104-L107)
4. `ETH` is the proposition $s_3 > 0$, and `ETHIsFalse` is its negation. [MainResults.lean, lines 109–122](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L109-L122)

The theorem `MainResults.ethIsFalse` has the type `MainResults.ETHIsFalse`. [Lines 11–13](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean#L11-L13) Since $s_3 \ge 0$, it says $s_3 = 0$. The source adds that this is equivalent to the following: for every $\delta > 0$ some machine decides 3-SAT within $c \cdot 2^{\delta n}$ steps. [MainResults.lean, lines 119–121](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L119-L121)

The source places this form in the literature. It cites Impagliazzo and Paturi for the hypothesis. It says that the accompanying paper defines the hypothesis as $s_k > 0$ for all $k \ge 3$, and that the paper notes that this is the same as $s_3 > 0$. [MainResults.lean, lines 109–112](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L109-L112)

## Second statement: the Main Theorem

Four more definitions are needed.

- The input word now carries $k$. It is $1^k 0$ followed by the word described above. [MainResults.lean, lines 137–139](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L137-L139)
- `numSat φ` is the number of satisfying assignments of $\varphi$ among all $2^n$ assignments. The output is this number in $n + 1$ bits, lowest bit first. [MainResults.lean, lines 129–135](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L129-L135)
- $\log$ is the logarithm to base $2$, not rounded. [MainResults.lean, lines 141–144](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L141-L144)
- The time bound is $T = \lfloor 2^{C \min\{E_m, E_n\}} \rfloor$, where $E_m = km/\sqrt{\log m}$ and $E_n = k^2 n \log\log n/\sqrt{\log n}$. [MainResults.lean, lines 146–154](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L146-L154)

`MainTheorem` says: there are one machine with finite alphabets and one natural number $C$ with the following property. For every $k \ge 1$, every $n \ge 4$ and every $k$-CNF $\varphi$ on $x_0, \dots, x_{n-1}$ that has $m \ge 2$ clauses and in which every variable occurs, the machine, started on the code of $(k, \varphi)$, halts within $T$ steps with the number of satisfying assignments of $\varphi$. [MainResults.lean, lines 156–160](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L156-L160) [MainResults.lean, lines 177–180](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L177-L180) The theorem `MainResults.mainTheorem` has this type. [Lines 15–17](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean#L15-L17)

Three points of the statement need care.

- **The order of the quantifiers.** The machine and $C$ come first. They do not depend on $k$, on $n$ or on the formula. [MainResults.lean, lines 162–163](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L162-L163) [MainResults.lean, lines 178–179](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L178-L179)
- **Every variable occurs.** Each of $x_0, \dots, x_{n-1}$ has to appear in some clause, positively or negatively. [MainResults.lean, lines 126–127](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L126-L127)
- **The thresholds.** The source explains that $m \ge 2$ and $n \ge 4$ are the least values with $\log m \ge 1$ and $\log\log n \ge 1$, and that one $C$ serves all of them. [MainResults.lean, lines 167–170](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L167-L170) It requires $k \ge 1$ because the paper defines $k$-CNFs only for $k \ge 1$. [MainResults.lean, lines 172–173](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L172-L173)

## How the two statements relate

Neither statement is written in terms of the other. The comment on the first theorem says that its proof derives it from the Main Theorem by two arguments. [Line 11](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/Challenge.lean#L11) The first statement is not a special case of the second. The Main Theorem covers only formulas in which every variable occurs, with $n \ge 4$ and $m \ge 2$. Its input word begins with $1^k 0$, which the input word of the first statement does not have. Its output is a count in $n + 1$ bits, where the first statement asks for one bit.

For $k = 3$ the second term of the minimum is $9 n \log\log n/\sqrt{\log n}$. This grows more slowly than $\delta n$ for every $\delta > 0$, and so does $C$ times it, because $C$ is fixed. The project README states both results: 3-SAT in time $2^{o(n)}$, and #3-SAT in time $2^{O(n \log\log n/\sqrt{\log n})}$. [README, line 3](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/README.md?plain=1#L3)

## What the statements leave out

- **Proofs.** This file has none.
- **Practice.** The README says that the result is purely asymptotic and says nothing about solving formulas in practice. [README, line 5](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/README.md?plain=1#L5)
- **Other inputs.** The Main Theorem says nothing about any other input word. That covers words for $k = 0$, formulas with a repeated clause or with a variable that does not occur, and formulas with fewer than two clauses or fewer than four variables. [MainResults.lean, lines 174–176](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L174-L176)
- **Other machine models.** The statements count steps of stack machines. The header of `MainResults.lean` argues that the bounds carry over to algorithms in the usual sense. It says that the facts used for this are standard and are not part of the Lean statements or proofs. [MainResults.lean, lines 36–48](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L36-L48)
- **Randomness.** Both statements are about deterministic machines. The source remarks, outside Lean, that refuting the deterministic form also refutes the randomized form. [MainResults.lean, lines 114–116](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/MainResults.lean#L114-L116)
- **Agreement with the paper.** The README says that Lean checks the proofs, but that no machine checks that `MainResults.lean` says what the paper says. [README, line 22](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/README.md?plain=1#L22)

## What I read

I read this file and `MainResults.lean` in full, and the Comparator configuration and the README, at the linked revision. I did not read the paper. I did not read the proofs, and I did not build the project.
