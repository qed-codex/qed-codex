---
{
  "module": "src/Development/AutomorphicArithmetic/CharacterBoxes/HostOfField.lean",
  "declarations": [
    "UpperTheory.Top.hostOfField",
    "UpperTheory.Top.supplyOfAdm"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Supply of abelian CM fields for a primitive Dirichlet character: character conditions and the kernel bound on long intervals of scales

[Theorem ANT.1.1770](https://andrewodesky.com/rh/lean/UpperTheory.Top.supplyChi/)

A scale $s=(x,\varepsilon,J)$, the number $b=\exp(x^{\varepsilon})$ formed from it, the supply condition and its conditions 1 to 16 are those of ([Properties of field data, their supply condition and their classes of families](https://andrewodesky.com/rh/lean/UpperTheory.Top.FReq/)). Hypothesis (abelian CM field with reciprocity map) and Hypothesis (fields and Galois data) are the two hypotheses of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), whose notation we use. Data satisfying the second hypothesis consist of data $\mathfrak E$ satisfying the first, with a finite abelian group $A$ and a number field $E$, of natural numbers $k,m,t$, of a finite set $T\subseteq A$, of a real constant $C_2$ and of further choices.

**The property $G_\psi$.** Let $\psi$ be a primitive Dirichlet character of order $o$, and let $\mathcal P_\psi$ be the set of primitive characters that induce the powers of $\psi$, defined in ([Weighted sums of regularized smoothed character sums](https://andrewodesky.com/rh/lean/Formalism.HC.Level/)). For a scale $s=(x,\varepsilon,J)$, data $\mathfrak E$ satisfying Hypothesis (abelian CM field with reciprocity map), a finite set $T\subseteq A$ and an integer $t\ge0$, the property $G_\psi(s,\mathfrak E,T,t)$ is the conjunction of the following two assertions.

(i) Hypothesis (character conditions) of ([Character and counting conditions at a single scale](https://andrewodesky.com/rh/lean/Formalism.HC.EAtH/)) holds for the set $\mathcal K=\mathcal P_\psi$, with no character $\xi$ chosen and with the integer $o$, for the field $\mathfrak E$ and the set $T$, at $x$, with the constants $\varepsilon$ and $C=4$.

(ii) The bound $\mathcal B\bigl(E,t,\exp(x^{\varepsilon}/2)\bigr)$ of ([Window condition: a bound on the Tate-Shafarevich groups of the twists Q\_l/Z\_l(-k) over auxiliary abelian fields](https://andrewodesky.com/rh/lean/UpperTheory.Top.VWin/)) holds.

**1.** Let $\psi$ be a primitive Dirichlet character. Suppose that the assertion that ([Window condition: a bound on the Tate-Shafarevich groups of the twists Q\_l/Z\_l(-k) over auxiliary abelian fields](https://andrewodesky.com/rh/lean/UpperTheory.Top.VWin/)) makes for every primitive Dirichlet character holds for $\psi$. Then the supply condition for $G_\psi$ with exponent $3/2$ holds.

**2.** Let $\varepsilon$ and $C_0$ be real numbers with $0<\varepsilon<1/52$ and $C_0\ge1$. There are real numbers $$C_2,\qquad C_8\ge C_0,\qquad c_6>0,\qquad C_b>0,\qquad x_0$$ with the following property. Let $s=(x,\varepsilon,J)$ be a scale with $x\ge x_0$ and $J\le C_0$. Let $\mathfrak E$ be data satisfying Hypothesis (abelian CM field with reciprocity map), with group $A$ of order $n$, integer $e$, element $a_0$ of order $n_0$, index $o=n/n_0$, primes $q,d$ and integer $Q_S$. Let $k,m,t$ be natural numbers that satisfy the parity conditions and the inequalities required of them in Hypothesis (fields and Galois data). Let $M\ge1$ be an integer and $Y$ a real number. Suppose that

(a) conditions 1 and 2 hold for $s$, $n$ and $k,m,t$;

(b) $o\le C_0$, $\ Q_S\le C_0n$, $\ M\le C_0$, and $Q_S$ divides $\operatorname{lcm}(2^{e+2},M)$;

(c) $x^{1/J}\le Y\le x$, and the assertion $\mathcal P_M(\varepsilon,Y,x;q,d)$ defined in ([Simultaneous auxiliary-prime and cohomological windows](https://andrewodesky.com/rh/lean/UpperTheory.Top.winPairs/)) holds;

(d) the data $\mathfrak E$ satisfy the field conditions at the integer $\lfloor Y^{\varepsilon/5}\rfloor$, in the sense of ([Field conditions at an integer and the completion property of an abelian CM field with reciprocity map](https://andrewodesky.com/rh/lean/HostParam.Seam.FieldRows/));

(e) the data $\mathfrak E$ have the completion property for $k,m,t$ defined in the same entry.

Then there are data satisfying Hypothesis (fields and Galois data) that consist of $\mathfrak E$, the integers $k,m,t$, the real constant $C_2$ and further choices, and there is a natural number $q_0$, such that conditions 3 to 16 hold for $s$ with the constants $C_2,C_8,c_6,C_b$ above and with $C_5=4$, and such that the set $T$ of these data satisfies $$\Bigl||T\cap(h+\langle a_0\rangle)|-\lambda(h)\,|T|\Bigr|\le x^{-1+\varepsilon}\,|T|\quad\text{for every }h\in A,\qquad\lambda(h)=\begin{cases}4/(3o+1),&h\in\langle a_0\rangle,\\3/(3o+1),&h\notin\langle a_0\rangle.\end{cases}$$

**3.** The sets $\mathcal Q(z)$ and $\mathcal D(z,z',q)$ of primes, good primes and good pairs are those of ([Good auxiliary primes and good pairs: uniform estimates for the twisted characters](https://andrewodesky.com/rh/lean/QH.GoodQ/)). There is a real number $C>0$ with the following property. Let $\varepsilon,\tau,K,\eta$ be real numbers with $0<\varepsilon<1/52$, $\tau>0$, $K\ge1$ and $\eta>0$, and let $N_0\ge1$ be an integer. There is a real number $Y_0\ge1$ such that the following holds for all real numbers $Y\ge Y_0$, $X\le Y^{K}$ and $z'$ with $$z(\log Y)^2\le z'\le K^2z(\log Y)^2,\qquad\text{where }z=Y^{\varepsilon/5}.$$ The set $\mathcal Q(z)$ is nonempty and has a subset $\mathcal Q'$ with $|\mathcal Q'|\ge(1-\eta)\,|\mathcal Q(z)|$ such that, for every $q\in\mathcal Q'$,

- the prime $q$ is good for $N_0,C,\tau,Y,X,z$;
- the set $\mathcal D(z,z',q)$ is nonempty and has a subset $\mathcal D'$ with $|\mathcal D'|\ge(1-\eta)\,|\mathcal D(z,z',q)|$ such that the pair $(q,d)$ is good for $N_0,C,\tau,Y,X,z,z'$ for every $d\in\mathcal D'$.
