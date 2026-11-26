---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/CmQuadraticFormEqAlternatingForm.lean",
  "declarations": [
    "GlobalTheory.Mem.Top.EvG"
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

## Contexts, and statements that hold eventually in the parameters

[Definition / hypothesis THETA.D025](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.Top.EvG/)

The construction depends on a list of real parameters that are chosen in a fixed order, each sufficiently large or small in terms of the earlier ones. "Eventually" abbreviates that order of quantifiers. This page fixes the parameters and the three forms of the quantifier.

**Parameters.**

- A *scale* is a triple $(x,\varepsilon,J)$ of real numbers with $x>1$, $0<\varepsilon<\frac1{52}$ and $J\ge1$.
- A *table of constants* $C$ is a record of about sixty real numbers. Its entries are arranged in four lists $C_{\mathrm{pre}}$ (one entry), $C_{\mathrm{out}}$ (sixteen), $C_{\mathrm{mid}}$ (ten) and $C_{\mathrm{last}}$ (thirty-two). The table is *standard* if twenty named entries have prescribed numerical values (for instance $2$, $405$, $\frac9{10}$, $12$, $377$, $25$, $401$), the entry called $C_8$ is at least $1$, one further entry is at least $1000$, and all entries of $C_{\mathrm{mid}}$ and $C_{\mathrm{last}}$ are at least $1$.
- Use the threshold rules and lower-bound convention in ([Fixed constants in an arithmetic family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.parConsts/)). For a context table, use its four ordered list formulas with $C_H=C_F$, replacing the final outgoing-list entry $\max(C_o,J)$ by $C_8$, the parameter denoted $C_p$ there. The table is *large for $K_0$* when these lower bounds hold.
- A *context* $\mathcal{K}$ consists of a scale, a standard table $C$, two further real numbers $c_D$ and $c_h$, and *preliminary data*: ranks $(k,m,t,n)$, a host field with its level primes, a finite set of words with their weights (these three as in [Datum of the construction and objects over it](https://andrewodesky.com/rh/lean/GlobalTheory.EX.OB.Obj/)), a prime $T(u)$ for every word $u$ that is the norm of an element of $\mathcal{O}_E$ lying in $K$, integers $a_\theta, b_\theta$, a level prime $q_1$, and a Boolean code that fixes the middle entries of the weights. The context includes the conditions that tie these to the scale, among them that $n$ lies between $x^{2+8\varepsilon}$ and $2x^{2+8\varepsilon}$ and $m$ between $\sqrt{x^{1-\varepsilon/8}}$ and $2\sqrt{x^{1-\varepsilon/8}}$. It also includes three equalities that fix the window in which each $T(u)$ lies; they involve the masses of the genera of the standard Hermitian lattices $\mathcal{O}_E^{k}$ and $\mathcal{O}_E^{r}$ (the mass of a genus is the sum of $1/|\mathrm{Aut}(M)|$ over representatives $M$ of its isometry classes) and the number $\exp(C_\Gamma m^5 f x^{\varepsilon})$, where $C_\Gamma$ is an entry of the table.
- A context is *good for* real numbers $(C_5,c_6,C_b)$ if, in addition, the host field satisfies a further list of size conditions involving these three constants and its set of level primes is $\{g_0,g_1,p_\delta,p_\delta',q_1\}$.

**Eventually.** Let $P$ be a property of contexts. *$P$ holds eventually* means:

\> there is $\varepsilon_0>0$ such that for all real $\varepsilon$, $C_8$, $C_5$, $c_6$, $C_b$ with $0<\varepsilon\le\varepsilon_0$, $\varepsilon<\frac1{52}$ and $C_8\ge1$ there is a threshold $K_0$ such that for every standard table $C$ with $C_8$-entry equal to $C_8$ that is large for $K_0$ there is $c_1$ such that for every $c_D\ge c_1$ there is $c_2$ such that for every $c_h\ge c_2$ there is $x_0$ such that $P(\mathcal{K})$ holds for every context $\mathcal{K}$ with table $C$, numbers $c_D$, $c_h$, scale parameter $\varepsilon$ and $x\ge x_0$ that is good for $(C_5,c_6,C_b)$.

Two variants occur. *Eventually for all contexts* is the same with the three numbers $C_5,c_6,C_b$ and the requirement that the context be good for them omitted; it is the stronger assertion. A second form, used for statements about attached records, lets the property depend also on the parameter tuple $\kappa=(\varepsilon,C,c_D,c_h,C_5,c_6,C_b)$ and assumes $C_5,c_6,C_b>0$; the order of quantifiers is the same.

**For large bases.** A *base* over a context adds to the preliminary data a coefficient field $\mathbb{L}$ with subfields $K_s\subseteq\mathbb{L}_0\subseteq\mathbb{L}$ and an embedding $\mathbb{L}\to\mathbb{C}$ (as in a datum; $K_s$ contains the image of $E$ and certain roots of unity). A *Hecke character* of a number field is a continuous homomorphism from its idele group to $\mathbb{C}^\times$ that is trivial on principal ideles. A *frame* for a base is a list of Hecke characters of $E$, namely $\mu_{0,1},\dots,\mu_{0,m}$, $\eta$, $\chi$, $\delta$, $\delta'$, each satisfying a defining condition, together with two auxiliary records. *Twist data* for a base consist of a finite set $\Pi$ of natural numbers and, for every finite place $w$ of $\mathbb{L}$ with residue characteristic $\ell$, a finite set $Q(w)$ of primes of $E$ not dividing $\ell$, an integer $k(w)\ge0$ and a Hecke character $\psi(w)$ of $E$ whose order divides $\ell^{k(w)}$; $\psi(w)=1$ and $k(w)=0$ when $\ell\notin\Pi$, and the data at $w$ and at its complex conjugate agree. Twist data are *untwisted* if every $Q(w)$ is empty, every $k(w)$ is $0$ and every $\psi(w)$ is trivial.

Let $P$ be a property of a context together with a base, a frame and twist data. *$P$ holds eventually for large bases* means that eventually, in the sense above, the following holds for the context $\mathcal{K}$: there are rules assigning to the preliminary data, the frame and the images of $K_s$ and $\mathbb{L}_0$ in $\mathbb{C}$ a finite set $S_1$ of algebraic numbers, a finite set $P_1$ of natural numbers, for every $\ell$ a finite set $A(\ell)$ of natural numbers, and (depending also on the set of characters occurring in the frame and the twist data) a finite set $S_2$ of algebraic numbers, such that $P$ holds for every base over $\mathcal{K}$, every frame and all twist data for which the image of $\mathbb{L}_0$ in $\mathbb{C}$ contains $S_1$, the image of $\mathbb{L}$ contains $S_2$, $P_1\subseteq\Pi$, and no prime in $Q(w)$ has absolute norm in $A(\ell)$.
