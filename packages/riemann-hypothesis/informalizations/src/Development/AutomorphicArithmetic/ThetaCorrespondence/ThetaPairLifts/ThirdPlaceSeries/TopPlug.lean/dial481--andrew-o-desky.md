---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean",
  "declarations": [
    "UpperTheory.Top.every_character_of_green_v_win",
    "UpperTheory.Top.zero_free_all_of_green_v_win"
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

## Zero-freeness for primitive Dirichlet characters: the deduction from the interval criterion, the bound on the scales of a family and the existence of families

[Theorem ANT.1.1768](https://andrewodesky.com/rh/lean/UpperTheory.Top.zero_free_all_of_green_v_win/)

Throughout, $L(s,\chi)$ is the $L$-function of ([Regularized smoothed character sums](https://andrewodesky.com/rh/lean/Deduction.Gchi/)), and $\mathcal P_\psi$, $G_{\mathcal K}$ are the set of characters and the weighted sum defined in ([Weighted sums of regularized smoothed character sums](https://andrewodesky.com/rh/lean/Formalism.HC.Level/)). Let $\mathcal K,\xi,o$ be as in that definition, and let $E_D,E_P$ be real numbers. An arithmetic family, in the sense of ([Arithmetic families with local and theta data](https://andrewodesky.com/rh/s/family-arithmetic-data.html)), *satisfies the family conditions for $\mathcal K,\xi,o$ with constants $E_D,E_P$* when it satisfies conditions (a) and (b) of part 2 of ([Weighted prime-sum bound](https://andrewodesky.com/rh/lean/UpperTheory.Comparison%E2%82%82.core_gm/)) for $\mathcal K,\xi,o$ and $E_D,E_P$. A set $\mathcal S$ of real numbers *contains long intervals of exponent $\lambda$*, for a real number $\lambda$, when for every real number $Y_0$ there is a real number $Y\ge\max\{1,Y_0\}$ with $[Y,Y^\lambda]\subset\mathcal S$.

**1.** Assume the following three assertions.

(i) The polynomial parametrization in ([Cuspidal characters of finite general linear groups](https://andrewodesky.com/rh/lean/GlobalTheory.greenRegularCharacters_holds/)): for every prime $p$, every integer $d\ge1$ and every choice of the map $\tau$ and of the generators $\gamma_e$ made there, there is a bijection $P\mapsto\chi_P$ from the set of monic irreducible polynomials $P\in\mathbb F_p[T]$ of degree $d$ with $P(0)\ne0$ onto the set of cuspidal characters of $\mathrm{GL}_d(\mathbb F_p)$ such that every $\chi_P$ has the degree and the values stated there.

(ii) The assertion of ([Window condition: a bound on the Tate-Shafarevich groups of the twists Q\_l/Z\_l(-k) over auxiliary abelian fields](https://andrewodesky.com/rh/lean/UpperTheory.Top.VWin/)).

(iii) There exist six pieces of data that satisfy the forty conditions of ([The record of conditions on a class of families that the final argument takes as input](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)).

Then, for every primitive Dirichlet character $\psi$, the function $L(s,\psi)$ has no zero in the half-plane $\Re s>1/2$.

**2.** Assume assertions (i), (ii) and (iii) of Statement 1. Then the assertion of ([Zero-freeness: no Dirichlet L-function vanishes in the half-plane Re s \> 1/2](https://andrewodesky.com/rh/lean/UpperTheory.EveryCharacter/)) holds: for every integer $N\ge1$, every Dirichlet character $\chi$ modulo $N$ and every $s\in\mathbb C$, $$\Re s>\frac12,\qquad(\chi\ne1\ \text{or}\ s\ne1)\quad\Longrightarrow\quad L(s,\chi)\ne0.$$

**3.** Let $\mathcal K,\xi,o$ be as in ([Weighted sums of regularized smoothed character sums](https://andrewodesky.com/rh/lean/Formalism.HC.Level/)), and let $\lambda$ be a real number. Suppose that the following three hypotheses hold.

*Hypothesis (bound).* Let $E_D,E_P$ and $\varepsilon>0$ be real numbers, and let $\mathcal F$ be an arithmetic family with exponent $\varepsilon$ and set of occupied scales $\mathcal W$. If $\mathcal F$ satisfies the family conditions for $\mathcal K,\xi,o$ with constants $E_D,E_P$, then there is a real number $x_1\ge1$ such that $$G_{\mathcal K}(x)\le x^{1/2+(E_D+E_P+7)\varepsilon}\qquad\text{for every }x\in\mathcal W\text{ with }x\ge x_1.$$

*Hypothesis (criterion).* Let $\theta$ be a real number with $0<\theta<1$. If the set of real numbers $x>0$ with $G_{\mathcal K}(x)\le x^\theta$ contains long intervals of exponent $\lambda$, then, for every $\chi\in\mathcal K$, the function $L(s,\chi)$ has no zero in the half-plane $\Re s>\theta$.

*Hypothesis (existence).* There are real numbers $E_D,E_P$ and $\varepsilon_1>0$ such that, for every real number $\varepsilon$ with $0<\varepsilon<\varepsilon_1$, there is an arithmetic family with exponent $\varepsilon$ that satisfies the family conditions for $\mathcal K,\xi,o$ with constants $E_D,E_P$ and whose set of occupied scales contains long intervals of exponent $\lambda$.

Then, for every $\chi\in\mathcal K$, the function $L(s,\chi)$ has no zero in the half-plane $\Re s>1/2$.

**4.** Let $\lambda>1$ be a real number and let $\mathcal Q$ be a set of primitive Dirichlet characters. Suppose that, for every $\psi\in\mathcal Q$, the following hold for $\mathcal K=\mathcal P_\psi$, with no character $\xi$ chosen and with $o$ the order of $\psi$: Hypothesis (bound); Hypothesis (criterion) with every real number $\lambda'>1$ in place of $\lambda$; and Hypothesis (existence) with the exponent $\lambda$. Then, for every $\psi\in\mathcal Q$, the function $L(s,\psi)$ has no zero in the half-plane $\Re s>1/2$.
