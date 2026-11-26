---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportSt.lean",
  "declarations": [
    "GlobalTheory.BigOn.SurjectiveOntoX"
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

## Transfer conditions and numerical bounds for the stage-zero construction

[Definition / hypothesis THETA.D091](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.S0.OpenParameterStatements/)

This entry uses the notions of datum, family, class, refinement and sufficiently constrained family from ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)), and point, attached record, selection and transfer from ([The norm bound at the primes 2 and 3 for the families produced by the construction with a given parameter](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.RL.LinkedAt/)). The latter entry defines transfer through a property of points and a link. Here the construction parameters may be arbitrary: they determine a built-point property, a good-point property and a link, just as in that entry. For a property $H$ of a class and a selection, say **$H$ transfers** if there is a property $R$ of points such that, eventually for large bases satisfying the base condition, every built point has $R$, and $H$ holds for the families produced through the good points satisfying $R$ and the link. The base condition and the internal construction are not expanded.

**Twelve open conditions.** Each of the following properties must transfer. In the first seven and the ninth, it is required at every member of every family of the class, for its selected record. In the eighth, tenth and eleventh it is required eventually at members of every sufficiently constrained family of the second refinement. In the twelfth it is required there for every sufficiently large real constant, above a nonnegative threshold depending on the family. The properties are:

1. Two conditions on the selected record, one on its realisation and one on separation of types (not expanded).
2. A condition on subspaces attached to the selected record (not expanded).
3. A condition relating lattices and pairings in the datum and the selected record (not expanded).
4. A condition comparing pairings at decomposition points; its form is given in item (8) of ([The record of conditions on a class of families that the final argument takes as input](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)).
5. Existence of a record relating the selected realisation to a choice of indices (the record is not expanded).
6. A compatibility condition on the selected record (not expanded).
7. Existence, at each selected record, of three objects with three compatibility conditions (the objects and conditions are not expanded).
8. A condition on the datum (not expanded).
9. Existence of a comparison object for the selected record satisfying four conditions, the fourth itself a conjunction of three conditions; these conditions are not expanded.
10. A condition on multiplicities in the selected realisation (not expanded).
11. A condition on numbers attached to the selected record (not expanded).
12. The definite-side condition of item (25) of ([The record of conditions on a class of families that the final argument takes as input](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)), with the two constants just quantified.

**Two numerical statements.** For all sufficiently constrained families satisfying an additional list of conditions (not expanded), consider points at members with $x>x_1$ that satisfy a point condition (not expanded). The first statement assumes the divisibility bound of ([A class of families satisfying the input conditions of the final argument exists, given hypothesis list A, the rationality test, the norm bound at 2 and 3, a maximal slope bound and a covolume bound](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt/)). It asserts the existence of $C_0\ge0$ such that, eventually at these members, for every such point satisfying three further conditions (not expanded) and every $C\ge C_0$, the following holds. For its finite set $T$ of places, indices $j$, tuples $\mu_w$, and numerical data $I_{j,t,w}, r_w, F_{w,j}, e_{w,j}, q_w, J_{t,w,j}, L_w, D, E$ (not expanded), $$\sum_j(I_{j,\mu_w,w}+I_{j,\mu_w,\bar w})\le D\left(\sum_j(2r_wF_{w,j}+r_we_{w,j})+\frac{2r_w}{q_w^2}\right),\quad e_{w,j}\ge0\quad(w\in T),$$ $$\sum_{w\in T}L_w\bigl(r_we_{w,j}+r_wJ_{\mu_w,w,j}\bigr)\le C E\quad\text{for every }j.$$ The second statement is the lower bound for the scalars of ([Admissible points over the members of a family, the row lattice of a point and its maximal slope](https://andrewodesky.com/rh/lean/GlobalTheory.BigTop.FamHyp/)): eventually at the admissible points of the family, for every real $C$, $$l_6(j)\le\log\lambda_{j,\mu_0,\pi,v}\quad\text{for all stages }j,\text{ full labels }\pi\text{ and infinite places }v.$$ That page defines the class of families, the admissible points, the numbers $l_6(j)$ formed with $C$, and the scalars $\lambda_{j,\mu_0,\pi,v}$. Both statements quantify over all sufficiently constrained families of the additional class, not merely over families arising from the construction. The first numerical statement has the inequalities displayed above; its body does not assert surjectivity.

**The 26 transferred conditions.** The conclusion of the theorem using this entry consists of the following assertions. Each uses the transfer quantifiers above, except for the placement of counting constants specified below. The first eleven concern properties of the class independent of selection: the class-number formula of item (10), the surjectivity of item (23), the mass and class assertions of item (22), and the seven eventual conditions of items (26)–(32), followed by the compatibility condition of item (37), all from ([The record of conditions on a class of families that the final argument takes as input](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)). These descriptions refer to the properties themselves; their quantifiers over families are those given in the cited items, except that the mass and class assertions here hold at every member of every family in the class.

The remaining fifteen are properties of the class with its selection. They comprise: a bound on the realisation and the condition of item (4); the five conditions (1)–(5) of the twelve open conditions above; two eventual conditions on the selection (not expanded); the serving condition of item (33); the surjectivity condition of item (36); the condition of item (14); a counting condition; the nine bounds and definite-side condition of item (25); and an arbitrary property $N$ of the second refinement of the class. All numbered items in this paragraph refer to ([The record of conditions on a class of families that the final argument takes as input](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)). For the counting condition, after the property $R$ of points is chosen, there are a function assigning counting constants to each finite list of reals and a number $c_I>0$, with $C_0\ge0$ and $2(C_{YL}+1)\le A_0$ for every family. The conjunction of two counting properties then holds for the families produced through the good points satisfying $R$: a count at every member using those constants (not expanded), and the existence of the objects and count of item (35), for all sufficiently constrained families of the second refinement. The other terms in these conditions are not expanded beyond the cited entry.
