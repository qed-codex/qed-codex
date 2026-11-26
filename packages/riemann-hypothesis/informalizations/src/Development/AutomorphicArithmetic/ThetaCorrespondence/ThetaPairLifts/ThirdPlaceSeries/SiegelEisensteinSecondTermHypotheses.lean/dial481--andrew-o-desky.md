---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean",
  "declarations": [
    "UpperTheory.Lit.every_character_of_theta_integrals_local_matching",
    "UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound"
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

## Non-vanishing of all Dirichlet L-functions for Re s \> 1/2, given the cited theorems, the covolume bound and a condition on every primitive character

[Theorem ANT.0006](https://andrewodesky.com/rh/lean/UpperTheory.Lit.every_character_of_theta_integrals_local_matching/)

Assume the following seven assertions.

1. The assertions in ([Hypothesis list A: sixty assumed statements on representations of p-adic and real groups, automorphic forms, Galois representations and class field theory](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses/)).
2. The assertions in ([Hypothesis list B: fifty-three assumed statements on Weil representations, theta lifts, discrete series, L-functions and complex multiplication](https://andrewodesky.com/rh/lean/GlobalTheory.FunPr.ThetaLocalInputs/)).
3. The assertion of ([Theta integrals agree: for a matching datum the two theta integrals are proportional on matching functions, with a unique nonzero constant, and the constant changes by an L-value when a hyperbolic plane is removed](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.ThetaIntegralsAgree/)).
4. The assertion of ([Local matching: a matching datum for two Hermitian spaces of complementary dimensions admits matched quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.LocalMatching/)).
5. The primary covolume assertion in ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)).
6. The assertion of ([Hypothesis: existence of a reciprocity map for GL\_n over the completions of number fields, with a restricted list of properties](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.RecTExists/)).
7. The assertion of ([Window condition: a bound on the Tate-Shafarevich groups of the twists Q\_l/Z\_l(-k) over auxiliary abelian fields](https://andrewodesky.com/rh/lean/UpperTheory.Top.VWin/)).

Then for every integer $N\ge1$, every complex Dirichlet character $\chi$ modulo $N$ and every $s\in\mathbb C$, $$\Re s>\frac12,\qquad (\chi\ne1\ \text{or}\ s\ne1)\quad\Longrightarrow\quad L(s,\chi)\ne0.$$

## A class of families satisfying the input conditions of the final argument exists, given hypothesis list A, the rationality test, the norm bound at 2 and 3, a maximal slope bound and a covolume bound

[Theorem ARAK.0007](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt/)

**Setting.** We use the following terms from other entries.

- From ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)): datum, size data, family, member, class of families $\mathcal{A}$, its second refinement $\mathcal{A}''$, and "holds for all sufficiently constrained families of a class". At a member $(x,i)$ we write $k,m,f$ for the numbers of its datum, $\Lambda$ for its coefficient field, $\varepsilon$ for the parameter of the family and $b=\exp(x^{\varepsilon})$.
- From ([Contexts, and statements that hold eventually in the parameters](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.Top.EvG/)): context, base, frame, twist data, "eventually for all contexts" and "holds eventually for large bases".
- From ([The norm bound at the primes 2 and 3 for the families produced by the construction with a given parameter](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.RL.LinkedAt/)): point, property of points, attached record, selection, selected record, link, "holds for the families produced through $(Q,\mathrm{Lk})$", the construction with a real parameter $c$ with its properties of points $Q^{\mathrm{built}}_c$, $Q^{\mathrm{good}}_c$ and its link $\mathrm{Lk}_c$, and the condition $\mathrm{NB}(c)$. That construction is defined only when ([Hypothesis: existence of a reciprocity map for GL\_n over the completions of number fields, with a restricted list of properties](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.RecTExists/)) holds.

**The construction restricted by a property.** Let $c$ be a real number and let $\mathcal{P}$ be a property of a context together with a base, a frame and twist data. In the construction with parameter $c$ a built point carries additional data. The *construction with parameter $c$ restricted by $\mathcal{P}$* requires two further items in that data: a proof of a condition on the components of the point that depends on $c$ (it asserts the existence of three records with four properties), and a proof that $\mathcal{P}$ holds for the context, base, frame and twist data of the point. Its properties of points $Q^{\mathrm{built}}_{c,\mathcal{P}}$, $Q^{\mathrm{good}}_{c,\mathcal{P}}$ and its link $\mathrm{Lk}_{c,\mathcal{P}}$ are defined as for the construction with parameter $c$.

**Statements at the points of a construction.** Let $H(\mathcal{A},\sigma)$ be a property of a class of families $\mathcal{A}$ with a selection $\sigma$ on it. We say that *$H$ holds at the points of the construction with parameter $c$ restricted by $\mathcal{P}$* if there is a property of points $R$ such that:

- (A) eventually for all contexts and for large bases, if the base and the frame satisfy a base condition, then every point over them that has the property $Q^{\mathrm{built}}_{c,\mathcal{P}}$ has the property $R$;
- (B) $H$ holds for the families produced through $(Q^{\mathrm{good}}_{c,\mathcal{P}}\text{ and }R,\ \mathrm{Lk}_{c,\mathcal{P}})$.

The condition $\mathrm{NB}(c)$ is the statement of the same form for the construction with parameter $c$, without restriction, and the norm bound at 2 and 3.

**Lattices attached to a selected record.** Let $(x,i)$ be a member of a family with $x>x_1$, and write $r_\infty$ for the number of infinite places of $\Lambda$. The selected record at the member determines the following objects (through a realisation in the sense of [Rational families of forms, their realisations by theta maps, and the rationality test](https://andrewodesky.com/rh/lean/Formalism.IndefR.Rat.RowTest/)):

- a natural number $\Delta$ and, for every infinite place $v$ of $\Lambda$, a complex $\Delta\times\Delta$ matrix $X_E(v)$ and a real number $\kappa_v$;
- a set of tuples; for every finite place $w$ of $\Lambda$ a tuple $\mu_w$; and for every tuple $t$ a natural number $d(t)$, an $\mathcal{O}_\Lambda$-submodule $A_t$ of $\Lambda^{d(t)}$ and a $\Lambda$-linear map $\iota_t\colon\Lambda^{d(t)}\to\Lambda^{\Delta}$;
- for each $j\in\{1,\dots,m\}$ a natural number $d_j$, complex $d_j\times d_j$ matrices $X_j(v)$ and an $\mathcal{O}_\Lambda$-submodule $M_j$ of $\Lambda^{d_j}$.

Let $R_E$ be the $\mathcal{O}_\Lambda$-submodule of $\Lambda^{\Delta}$ that agrees locally at each finite place $w$ with the image of the lattice of the tuple $\mu_w$: $$R_E=\bigl\{\,y\in\Lambda^{\Delta}\ :\ \text{for every finite place } w \text{ there is } s\in\mathcal{O}_\Lambda\smallsetminus\mathfrak{p}_w \text{ with } s\,y\in\iota_{\mu_w}(A_{\mu_w})\,\bigr\}.$$

**Maximal slope.** For $y\in\Lambda^{\Delta}$ and an infinite place $v$ let $y_v\in\mathbb{C}^{\Delta}$ be the image of $y$ under the embedding chosen for $v$, and let $\phi(y)=\bigl(X_E(v)^{-1}y_v\bigr)_v$, an element of the real Euclidean space $\prod_v\mathbb{C}^{\Delta}$ with its standard inner product. For a nonzero $\mathcal{O}_\Lambda$-submodule $N$ of $\Lambda^{\Delta}$ put $$\mu(N)=-\frac{2\log\operatorname{covol}\phi(N)}{\operatorname{rank}_{\mathbb{Z}}\phi(N)}-\log 2+\frac{\log|\operatorname{disc}\Lambda|}{[\Lambda:\mathbb{Q}]},$$ where $\operatorname{covol}$ is the square root of the Gram determinant of a $\mathbb{Z}$-basis, and let $$\mu_{\max}(R_E)=\sup\{\mu(N)\ :\ N\subseteq R_E \text{ a nonzero } \mathcal{O}_\Lambda\text{-submodule}\}.$$ Since $\Lambda$ is totally complex, $\mu(N)$ is the negative of the normalised logarithmic covolume of $N$, as defined in ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)), divided by the rank of $N$ over $\mathcal{O}_\Lambda$.

**The maximal slope property $H_{\mathrm{slope}}$.** A family *satisfies the divisibility bound* if there are real numbers $C$ and $x_0$ such that at every member with $x\ge x_0$ and for every $j\in\{1,\dots,m\}$, $$\sum_{w}\frac{\log\mathrm{N}w}{[\Lambda:\mathbb{Q}]}\,e_w\,\eta_j(w)\ \le\ D_0\cdot C\,x^{\varepsilon}\bigl(f\,m\,b\,x^{\varepsilon}+N_c\bigr).$$ Here $w$ runs over the places of $\Lambda$ in the finite set of the size data whose tuple differs from the base tuple, $e_w$, $\eta_j(w)$ and $N_c$ are as in condition (40) of ([The record of conditions on a class of families that the final argument takes as input](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)), and $D_0$ is a natural number of the datum.

$H_{\mathrm{slope}}(\mathcal{A},\sigma)$ is the statement: for all sufficiently constrained families $\mathrm{Fm}$ of $\mathcal{A}''$, with the real number $C_H$ of that definition, if $\mathrm{Fm}$ satisfies the divisibility bound then there is $x_0$ such that at every member with $x\ge x_0$ and $x>x_1$ the selected record satisfies $$\mu_{\max}(R_E)\ \le\ x^{C_H}\,b\ -\ \frac{1}{r_\infty}\sum_{v}\log\kappa_v .$$

**The covolume property $H_{\mathrm{cov}}$.** $H_{\mathrm{cov}}(\mathcal{A},\sigma)$ is the statement: for all sufficiently constrained families of $\mathcal{A}''$ there is $C_0\ge 0$ such that for every $C\ge C_0$ there is $x_0$ such that at every member with $x\ge x_0$ and $x>x_1$, for every $j\in\{1,\dots,m\}$, $$\frac{2\log H_\Lambda(M_j)}{[\Lambda:\mathbb Q]\Delta}\le P_j+C fmbx^\varepsilon\log\log x.$$ Here $H_\Lambda(M_j)$ is the arithmetic covolume and $P_j$ the weighted period term defined in ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)), applied to the lattices of the selected record. The integer $\Delta$ is the dimension of its distinguished theta-image space.

Assume the following.

1. The conditions of ([Hypothesis list A: sixty assumed statements on representations of p-adic and real groups, automorphic forms, Galois representations and class field theory](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses/)) hold.
2. The rationality assertion in hypothesis 2 of ([Mass ratio of the standard Hermitian lattices over a CM field, and existence of built points and of their attached theta-lift records carrying a prescribed eventual property](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.StageOneU.member_bundles_large_unramified_exponents_alt/)).
3. ([Hypothesis: existence of a reciprocity map for GL\_n over the completions of number fields, with a restricted list of properties](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.RecTExists/)) holds.

Let $c$ be a real number and let $\mathcal{P}$ be a property of a context together with a base, a frame and twist data. Assume further:

4. $\mathcal{P}$ holds eventually for large bases.
5. $\mathrm{NB}(c)$ holds.
6. $H_{\mathrm{slope}}$ holds at the points of the construction with parameter $c$ restricted by $\mathcal{P}$.
7. $H_{\mathrm{cov}}$ holds at the points of the construction with parameter $c$ restricted by $\mathcal{P}$.

Then there exists a record of the kind defined in ([The record of conditions on a class of families that the final argument takes as input](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)): a class $\mathcal{A}$ of families, a selection $\sigma$ on $\mathcal{A}$, functions $c_T$ and $c_{30}$, a further record at every member, and a real number $c_I$, such that the forty conditions of that entry hold.

**Criterion using theta integrals.** Assume the following seven assertions.

1. The assertions in ([Hypothesis list A: sixty assumed statements on representations of p-adic and real groups, automorphic forms, Galois representations and class field theory](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses/)).
2. The assertions in ([Hypothesis list B: fifty-three assumed statements on Weil representations, theta lifts, discrete series, L-functions and complex multiplication](https://andrewodesky.com/rh/lean/GlobalTheory.FunPr.ThetaLocalInputs/)).
3. The assertion of ([Theta integrals agree: for a matching datum the two theta integrals are proportional on matching functions, with a unique nonzero constant, and the constant changes by an L-value when a hyperbolic plane is removed](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.ThetaIntegralsAgree/)).
4. The assertion of ([Local matching: a matching datum for two Hermitian spaces of complementary dimensions admits matched quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.LocalMatching/)).
5. The primary covolume assertion in ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)).
6. The assertion of ([Hypothesis: existence of a reciprocity map for GL\_n over the completions of number fields, with a restricted list of properties](https://andrewodesky.com/rh/lean/UpperTheory.Zero.LLC.RecTExists/)).
7. For every real number $c$, the condition $\mathrm{NB}(c)$ of ([The norm bound at the primes 2 and 3 for the families produced by the construction with a given parameter](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.RL.LinkedAt/)) holds, with the construction formed using assertion 6.

Then the same existence conclusion holds.
