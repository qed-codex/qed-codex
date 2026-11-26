---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/CountVOf.lean",
  "declarations": [
    "UpperTheory.V.UnitaryThreeInertia.countV_of_finiteness_duality_euler_host"
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

## Selmer lengths and trace congruences over the Gaussian field

[Theorem AGR.1.1778](https://andrewodesky.com/rh/lean/UpperTheory.V.UnitaryThreeInertia.countV_of_finiteness_duality_euler_host/)

The constants $N_\chi$, $o$, $p_K$, $h_K$ and $p_1$ of a primitive Dirichlet character $\chi$, its set of primes $\mathcal B_\chi$, the auxiliary triples $(\nu,q,d)$ for $\chi$ and their moduli, the sets $\mathscr X_{\mathcal O}(e)$ of Dirichlet characters, and, for a Dirichlet character $\psi$ and an odd prime $\ell$, the character $\psi^\dagger$, the exponent $c_2(\psi)$ and the integer $n_0$ are defined in ([Auxiliary moduli of a primitive Dirichlet character and their characters](https://andrewodesky.com/rh/lean/Formalism.HC.PChar/)). The Selmer length of $(\epsilon_\ell^e\psi)^{-1}$ formed with $\mathcal O$ and $N$, and the number $e_{\mathcal O}$, are defined in ([Selmer lengths of twisted Dirichlet characters and Estimate I](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.CountI/)). The following notions are defined in ([Lifts of a sum of three characters with the sign character of the Gaussian field: deformation data, universal lifts and points](https://andrewodesky.com/rh/lean/UpperTheory.V.UnitaryThreeInertia.HostData/)): coefficient rings; admissible triples $(\ell,e,\psi)$; the deformation data $\mathfrak F$ for $(\Omega,\ell,\mathcal O,N,e,\psi)$, with their group $\Gamma$ and their characters $\eta$ and $\Psi$; marked elements of $\Gamma$; the universal lifts $(R,u)$ for $\mathfrak F$ at an element $g_1$, with the modules $R_j(u)$ and the algebra $E(u)$; and, for a homomorphism $r:\Gamma\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ with matrix part $\dot r$, the properties of being obtained from $u$, of being a characteristic-zero lift for $\mathfrak F$ at $g_1$, of being irreducible on $\ker\eta$ and of being rigid for $\mathfrak F$, and the condition $\mathcal P_K(\iota;r)$.

**Theorem.** Assume the hypotheses (H1)–(H13) listed below. For every primitive Dirichlet character $\chi$ there is a natural number $C$ with the following property. Let $(\nu,q,d)$ be an auxiliary triple for $\chi$, with modulus $N$, and let $t\ge2$ be an integer such that $q$ and $d$ are both larger than each of the six numbers $$2t+1,\qquad N_\chi,\qquad o,\qquad p_K,\qquad h_K,\qquad p_1.$$ Let $\Omega$ be an algebraic closure of $\mathbb Q$, $\ell\in\mathcal B_\chi$ an odd prime, $\mathcal O$ a coefficient ring for $\ell$, and $\psi\in\mathscr X_{\mathcal O}(1)$ a character such that $$16\,o\,(\ell N_\chi)^2\,4^{\,n_0}\le2^{\,c_2(\psi)}.$$ Then the Selmer length $L$ of $(\epsilon_\ell\psi)^{-1}$ formed with $\mathcal O$ and $N$ is finite, and $$\frac L{e_{\mathcal O}}\,\log\ell\le(\ell N)^C.$$

**Hypotheses of the theorem.**

- (H1) Hypothesis (A) below holds.
- (H2) The assertion of the theorem ([Cotangent length bounded by valuations at graded orbits](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.M.main_holds/)) holds.
- (H3) The assertion of the theorem ([Lengths of modules of liftable derivations bounded by a cotangent length](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.M.mprime_holds/)) holds.
- (H4)–(H8) Assertions (2), (3), (4), (5) and (6) of ([Local and global cohomological hypotheses](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.LiteralAutomorphy.LitCoh/)) hold.
- (H9) Assertion (1) of ([Local and global cohomological hypotheses](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.LiteralAutomorphy.LitCoh/)) holds.
- (H10) Hypothesis (V) below holds.
- (H11) Hypothesis (X) below holds.
- (H12) Hypothesis (R) below holds.
- (H13) Hypothesis (T) below holds.

In the five hypotheses that follow, *data* means: an algebraic closure $\Omega$ of $\mathbb Q$, a prime $\ell$, a coefficient ring $\mathcal O$ for $\ell$, integers $N\ge1$ and $e\ge0$, a Dirichlet character $\psi$ modulo $N$ with values in $\mathcal O$ such that the triple $(\ell,e,\psi)$ is admissible, and a deformation datum $\mathfrak F$ for $(\Omega,\ell,\mathcal O,N,e,\psi)$. The letter $K$ stands for a field of degree $2$ over $\mathbb Q$ that contains a square root of $-1$, and $\iota$ for an isomorphism of fields $\overline{\mathbb Q}_\ell\to\mathbb C$.

**Hypothesis (A).** For every $K$, all data and every $\iota$ there is a marked element $g_1\in\Gamma$ such that every universal lift $(R,u)$ for $\mathfrak F$ at $g_1$ has the following two properties.

1. The $\mathcal O$-module $R_0(u)$ is finitely generated.
2. Every homomorphism $r:\Gamma\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ that is obtained from $u$ by a homomorphism of $\mathcal O$-algebras $E(u)\to\overline{\mathbb Q}_\ell$ and is irreducible on $\ker\eta$ satisfies $\mathcal P_K(\iota;r)$.

**Hypothesis (V).** For all data, the deformation datum $\mathfrak F$ has property (V).

**Hypothesis (X).** For all data such that $$2\,\ell\,\mathfrak f\,4^{\,n_0}\le2^{\,c_2(\psi)},$$ where $\mathfrak f$ is the conductor of $(\psi^\dagger)^2$, the residual Selmer group of weight $-2$ of $\mathfrak F$ is zero.

**Hypothesis (R).** For every $K$, all data, every $\iota$ and every marked element $g_1\in\Gamma$, every characteristic-zero lift $r$ for $\mathfrak F$ at $g_1$ that satisfies $\mathcal P_K(\iota;r)$ is rigid for $\mathfrak F$.

**Hypothesis (T).** For every $K$ there is a natural number $C_K$ with the following property. For all data, every $\iota$ and every marked element $g_1\in\Gamma$, let $\mathcal R$ be the set of the characteristic-zero lifts $r$ for $\mathfrak F$ at $g_1$ that are irreducible on $\ker\eta$ and satisfy $\mathcal P_K(\iota;r)$. Then there is an element $\varphi\in\Gamma$ such that, with $\tau=\Psi(\varphi)+1+\Psi(\varphi)^{-1}$, $$\operatorname{tr}\dot r(\varphi)\ne\tau\qquad\text{for every }r\in\mathcal R,$$ and such that every finite subset $X\subset\mathcal R$, no two distinct members of which are isomorphic on $\ker\eta$, satisfies $$\log\ell\,\sum_{r\in X}v_\ell\bigl(\operatorname{tr}\dot r(\varphi)-\tau\bigr)\le(\ell Ne)^{C_K}.$$
