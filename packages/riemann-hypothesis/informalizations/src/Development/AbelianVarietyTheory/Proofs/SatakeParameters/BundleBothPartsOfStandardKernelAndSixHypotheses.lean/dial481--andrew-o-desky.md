---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/BundleBothPartsOfStandardKernelAndSixHypotheses.lean",
  "declarations": [
    "GlobalTheory.Svd.servH_row"
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

## Standard kernel records satisfy the kernel-entry conditions and the twisted system condition over all families, under six statements on elliptic curves with complex multiplication

[Theorem AV.0029](https://andrewodesky.com/rh/lean/GlobalTheory.Svd.servH_row/)

**Setting.** "Datum", "object", $E$, $K$, "inert in $K$" are as in ([Datum of the construction and objects over it](https://andrewodesky.com/rh/lean/GlobalTheory.EX.OB.Obj/)); "point", "property of points", "built by the recipe", "attached record", "link", "holds at all linked records", "family", "class", "selection" and "holds over the $Q$-points" are as in ([Points of the construction, properties of points, attached records and statements over families](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.Row/)).

*Kernel records.* A kernel record for an object $O$ over a datum $D$ is a compatible kernel realization for its given divisor data, twisted chains and integral comparisons, as defined in ([Compatible kernel realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Ker.KerEntTied/)). Its entries are the rational kernel entries of ([Rational kernel entries and derivative minors](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.KerEnt/)).

**Hypotheses on elliptic curves.** Write $K$ for the imaginary quadratic field $E_0$ in ([Ideal characters and period lattices](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TaylorLogMetric.Tor/)). In each of (E1) to (E6), $D$ is an arbitrary datum, and $\mathfrak c,\delta$ satisfy the ideal and discriminant-scalar conditions in ([Ideal characters and period lattices](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TaylorLogMetric.Tor/)). In (E1), (E4), (E5), (E6), let $B$ be any curve base consisting of the period pair, distinguished half-period, isometries and prime-indexed choices of ([Standard period bases for kernel theta functions](https://andrewodesky.com/rh/lean/Formalism.L2.Ker.IsoKG/)), for $(D,\mathfrak c,\delta)$, and let $\chi$ be any function on ideal labels satisfying the multiplicativity and norm-one principal-ideal formula in ([Ideal characters and period lattices](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TaylorLogMetric.Tor/)).

- (E1) *Algebraicity.* For every admitted pair of lattices, the Taylor coefficients, at every torsion point, of the function attached to the pair, to $B$ and to $\chi$ are algebraic numbers.
- (E2) *Models at inert primes.* For every prime $p\ge5$ inert in $K$ and every embedding $\lambda\colon\overline{\mathbb{Q}}\to\mathbb{C}_p$ there are $\mathfrak{c}',\delta'$ with $\Lambda(\mathfrak{c}',\delta')=\Lambda(\mathfrak{c},\delta)$, with $\mathrm{N}\mathfrak{c}'$ prime to $p$, and a change of variables over $\mathbb{C}_p$ after which the Weierstrass equation of $\mathbb{C}/\Lambda$, transported by $\lambda$, has all five coefficients in a fixed subring $W_p\subset\mathbb{C}_p$, and such that the logarithm of the resulting formal group is, up to a unit of $W_p$, obtained from a fixed formal logarithm by composition with a power series over $W_p$ with zero constant term and unit linear term.
- (E3) *Dictionary.* For every prime $l\ge5$ inert in $K$ and every model as in (E2) there are elements $g_2,g_3,\epsilon,s_2$ of the maximal unramified extension of $\mathbb{Q}_l$ such that $g_2,g_3$ are the invariants of the model, $\epsilon$ is the inverse of the constant of the formal isomorphism, a power series attached to $(\lambda,\Lambda)$, rescaled, equals a constant times a power series attached to the model and $s_2$, a product of two of the constants has absolute value $1$, and two further conditions hold, one of them for every datum.
- (E4) *Integrality at inert primes.* For every prime $p\ge5$ with $\left(\frac{-d}{p}\right)=-1$, every $\lambda\colon\overline{\mathbb{Q}}\to\mathbb{C}_p$ and every admitted pair of lattices in $E^N$, $E^{N'}$, an integrality statement at $p$ holds for the function of (E1).
- (E5) *Admissibility at inert places.* For every object over $D$ with a kernel record, every word $u$, tuple $\mu$ and finite place $w$ of $\mathbb{L}$ whose residue characteristic $p$ is a prime $\ge5$ of inert class for the host field, satisfies a non-vanishing condition, is not a level prime and does not divide $T(u)$, and for local data at $w$ of about thirty kinds: if five conditions on these local data hold (a curve condition relating them to $\mathfrak{c}$, $\delta$, a model as in (E2), $B$, $\chi$ and $\lambda$; three conditions on the local system; and a tie with the kernel record for every $j<m$), then the local system at $w$ and its pending data are admitted.
- (E6) *Existence of curve data.* For every prime $p\ge5$ inert in $K$ and prime to $\mathrm{N}\mathfrak{c}$ and every $\lambda\colon\overline{\mathbb{Q}}\to\mathbb{C}_p$ there is a model as in (E2), with its formal isomorphism, satisfying the curve condition used in (E5) for $(D,p,\mathfrak{c},\delta,B,\chi,\lambda)$.

The notions "admitted", "the function attached to", "integrality statement", "local data", "pending data" and "curve condition" are definitions of the formalization that were not opened; (E1) to (E6) are stated here as far as their first level was read.

Assume (E1) to (E6). Let a type of attached records, a property of points $Q$ and a link be given, together with a rule $\ker$ assigning to every attached record over $(D,O,c)$ a kernel record for $O$. Assume:

1. every $Q$-point is built by the recipe and carries, for its column input and later stages, a certificate of nine items (pinning, column data, a tie of tuples, three identifications, and a kernel family with two compatibility conditions);
2. *standardness holds at all linked records*: for every linked record $b$ the triple formed by its datum, its object and the kernel record $\ker(b)$ is equal to one obtained from a base, a column input with its laws and later stages, for which nine conditions hold: the column input is valid and pinned, is of twisted kind and contains its jets; the twisted forms of the object are those of the column input; the kernel record is the standard one of the column input; its entries are of the constructed form; it is adapted; and it is pinned at the top.

Then the conjunction of (a) and (b) below, as a property of a class $\mathcal{A}$ of families and a selection $\sigma$ for $\mathcal{A}$, holds over the $Q$-points:

- (a) there is $\varepsilon_1>0$ such that for every $0<\varepsilon\le\varepsilon_1$ there is a threshold $K_0$ such that every family in $\mathcal{A}$ with parameter $\varepsilon$ whose constants are large for $K_0$ satisfies the *twisted system condition*: there is $x_0$ such that for all $x\ge x_0$ above the threshold $x_1$ of the family and all indices $i$ there is a choice of local levels and chains for which the lattice comparison of the object at $(x,i)$ is compatible with its twisted forms and a system condition on its size data, group instances, constants, divisor data, levels and error terms holds with constant $1$;
- (b) for every family in $\mathcal{A}$, every $x>x_1$ and every index $i$, the entries of the kernel record $\ker(\sigma(x,i))$ satisfy the ten *kernel-entry conditions*: four conditions on the entries themselves, and, for some choice of three auxiliary data, six conditions on the local data derived from the entries (two evenness conditions, an orbit bound, a jet integrality condition and two shape conditions).

The twisted system condition and the ten kernel-entry conditions are conditions of the formalization that were not opened.
