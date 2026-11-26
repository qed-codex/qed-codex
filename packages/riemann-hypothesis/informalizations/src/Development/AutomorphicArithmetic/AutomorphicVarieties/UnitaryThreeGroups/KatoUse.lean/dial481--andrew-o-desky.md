---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/KatoUse.lean",
  "declarations": [
    "UpperTheory.V.U3.CorGK"
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

## Selmer lengths and trace congruences

[Theorem AGR.1123](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy/)

The characters $\psi_\ell$ and $\Psi=\epsilon_\ell^e\psi$, the Selmer length $L$ of $\Psi^{-1}$, the number $e_{\mathcal O}$ and the valuation $v_\ell$ are defined in the introduction. The class $\mathcal R(\iota,e,N)$ of three-dimensional representations of $G_K$ is defined in ([Level, attachment and comparison conditions on l-adic Galois representations](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.Level/)).

**Theorem.** Assume the hypotheses (H1)–(H9) listed below. Let $K\subset\overline{\mathbb Q}$ be an imaginary quadratic field, $\ell$ a prime, $\mathcal O\subset\overline{\mathbb Q}_\ell$ a discrete valuation ring that is finite over $\mathbb Z_\ell$, $N\ge1$ and $e\ge0$ integers, and $\psi$ a Dirichlet character modulo $N$ with values in $\mathcal O$. Assume the following four conditions.

1. $\ell\ne2$, $e\ge1$, $\ell-1\nmid2e$, and $N$ is even.
2. $\ell\nmid\operatorname{ord}\psi$, $\psi_\ell^2=1$, and $\psi(-1)=(-1)^e$.
3. $\ell\nmid|\operatorname{disc}K|\,h_K$, where $h_K$ is the class number of $K$, and $\gcd(N,|\operatorname{disc}K|)=1$.
4. $\ker\bar\epsilon_\ell\cap\ker(\psi\psi_\ell^{-1})\not\subset G_K$, where $\bar\epsilon_\ell:G_{\mathbb Q}\to\mathbb F_\ell^\times$ is the cyclotomic character modulo $\ell$.

Let $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$ be an isomorphism of fields, let $\sigma\in G_K$, and put $t=\Psi(\sigma)+1+\Psi(\sigma)^{-1}$. Suppose that $$\operatorname{tr}\rho(\sigma)\ne t\qquad\text{for every }\rho\in\mathcal R(\iota,e,N).$$ Then $L$ is finite, and there is a finite set $X\subset\mathcal R(\iota,e,N)$, no two distinct members of which are isomorphic, such that $$\frac L{e_{\mathcal O}}\le2\sum_{\rho\in X}v_\ell\bigl(\operatorname{tr}\rho(\sigma)-t\bigr).$$

**Hypotheses of the theorem.**

- (H1) Assertions (1)–(6) and (9)–(12) of ([Local and global cohomological hypotheses](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.LiteralAutomorphy.LitCoh/)) hold, and a uniform bound holds in the sense of ([A uniform bound for second cyclotomic cohomology](https://andrewodesky.com/rh/lean/UpperTheory.V.LemmaK/)).
- (H2) The assertion of the theorem ([Cotangent length bounded by valuations at graded orbits](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.M.main_holds/)) holds.
- (H3) The assertion of the theorem ([Lengths of modules of liftable derivations bounded by a cotangent length](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.M.mprime_holds/)) holds.
- (H4) The assertion of the theorem ([A homogeneous presentation for a framed deformation problem](https://andrewodesky.com/rh/lean/UpperTheory.V.Alg.lemmaP/)) holds.
- (H5) The conclusion of ([Vanishing of two rank-two Selmer groups](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH/)) holds for all data that satisfy conditions 1–10 of that theorem.
- (H6), (H7), (H8) Hypotheses (P1), (P2) and (P3) of ([Hypotheses on the points of the deformation rings of a sum of three characters](https://andrewodesky.com/rh/lean/UpperTheory.V.Th.RigidityFirstCase/)) hold.
- (H9) The assumption of ([An automorphy assumption for specializations with unramified coefficients](https://andrewodesky.com/rh/lean/UpperTheory.V.Aut.AutomorphyUnramifiedCoefficientsAlt/)) holds.

**Hypothesis (T).** For every imaginary quadratic field $K$ there are natural numbers $c$ and $A$ with the following property. Let $e\ge1$ and $N\ge1$ be integers, let $p\ge7$ be a prime with $p\nmid N\operatorname{disc}K$, let $w$ be a prime of $K$ above $p$, and let $q_w$ be the cardinality of its residue field. Let $(z_i)_{i\in I}$ be a finite family of roots of unity in $\mathbb C$ such that, for every automorphism $\tau$ of the field $\mathbb C$, there is a permutation $u$ of $I$ with $z_{u(i)}=\tau(z_i)$ for all $i\in I$. Then there is a nonzero integer $\Delta$ with $$\log|\Delta|\le c\,|I|\,\bigl(N(e+1)\bigr)^A\log p$$ such that the following holds for every prime $\ell\notin\{2,p\}$, every algebraic closure $\overline{\mathbb Q}$ of $K$, every isomorphism of fields $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$, every place $B$ of $\overline{\mathbb Q}$ above $w$, every Frobenius element $s\in G_K$ at $B$, and every family $(X_i)_{i\in I}$ of finite subsets of $\mathcal R(\iota,e,N)$ such that no $X_i$ contains two distinct isomorphic representations. Put $t_i=\iota^{-1}\bigl(q_w^{-e}z_i+1+q_w^{e}z_i^{-1}\bigr)$. Then $\operatorname{tr}\rho(s^{-1})\ne t_i$ for all $i\in I$ and $\rho\in X_i$, and $$|\Delta|_\ell\le\prod_{i\in I}\ \prod_{\rho\in X_i}\bigl|\operatorname{tr}\rho(s^{-1})-t_i\bigr|_\ell.$$

**Corollary.** Assume (H1)–(H9) and Hypothesis (T). For every number field $K$ there are natural numbers $c_5$ and $A$ with the following property. Let $\overline{\mathbb Q}$ be an algebraic closure of $\mathbb Q$ and $K\to\overline{\mathbb Q}$ an embedding, by which $K$ is regarded as a subfield of $\overline{\mathbb Q}$. Let $e\ge0$ and $N\ge1$ be integers, $H$ a subgroup of $(\mathbb Z/N\mathbb Z)^\times$, and $p\ne p'$ primes that do not divide $30N\operatorname{disc}K$. For every prime $\ell$ let $\mathcal O_\ell\subset\overline{\mathbb Q}_\ell$ be a discrete valuation ring that is finite over $\mathbb Z_\ell$, and let $\mathscr X_\ell(H)$ be the set of Dirichlet characters modulo $N$ with values in $\mathcal O_\ell$ whose kernel, as characters of $(\mathbb Z/N\mathbb Z)^\times$, is $H$. Let $\mathcal S$ be a finite set of primes such that, for every $\ell\in\mathcal S$, the field $K$ is imaginary quadratic and conditions 1–4 of the theorem hold for $K$, $\ell$, $\mathcal O_\ell$, $N$, $e$ and at least one $\psi\in\mathscr X_\ell(H)$. For $\ell\in\mathcal S$ and $\psi\in\mathscr X_\ell(H)$ write $L_{\ell,\psi}$ for the Selmer length of $(\epsilon_\ell^e\psi)^{-1}$ formed with $\mathcal O_\ell$ and $N$. Then every $L_{\ell,\psi}$ is finite, and $$\sum_{\ell\in\mathcal S}\log\ell\sum_{\psi\in\mathscr X_\ell(H)}\frac{L_{\ell,\psi}}{e_{\mathcal O_\ell}}\le2c_5\,\varphi\bigl([(\mathbb Z/N\mathbb Z)^\times:H]\bigr)\bigl(N(e+1)\bigr)^A\bigl(\log p+\log p'\bigr),$$ where $\varphi$ is Euler's function.
