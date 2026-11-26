---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamCol.lean",
  "declarations": [
    "GlobalTheory.AdForm.TwStdAlt"
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

## Conditions on a family and its realisation for the period identity

[Definition / hypothesis THETA.D029](https://andrewodesky.com/rh/lean/GlobalTheory.Fam.AllFamilyConditions/)

These conditions concern a datum as in ([Datum of the construction and objects over it](https://andrewodesky.com/rh/lean/GlobalTheory.EX.OB.Obj/)), together with a family indexed by tuples, spectral data, and a realisation of the family. The data specifying the family, the spectral data and the realisation are not expanded.

The conditions have six groups. The following descriptions do not specify every condition in those groups.

1. The first group includes the normalizations for the given realisation in ([Compatibility of recursive coordinate realizations](https://andrewodesky.com/rh/lean/Formalism.IndefR.IndefiniteRealisation/)), further conditions on the realisation at the base level and on its level structure (not expanded), an existence condition (not expanded), and an equality between the range of a linear map and a space of forms (the map and space are not expanded). The tuple index set is finite. If two primes of $E$ occur in one of the sets attached to tuples and have the same prime below in $F$, they are equal. The group includes a coprimality condition at primes in these sets, in another distinguished set, or containing one of the numbers attached to words (not expanded). It also requires the weight gap in item 9 of ([Conditions on linked records for the period identity](https://andrewodesky.com/rh/lean/GlobalTheory.Fam.BundlePointConditions/)).
2. The second group includes conditions on the base and on the existence of compatible auxiliary data, equalities of characters, and a leading-coefficient condition. The definitions of these conditions and characters are not expanded. The leading-coefficient condition has the form: there is a group element such that, for every word, a linear map exists with specified level and coefficient identities.
3. For each tuple, a character is a Hecke character and its local values agree with those of the character attached to the corresponding tuple in the base data; the associated sets of primes agree. For each word there is a linear map satisfying the leading-coefficient condition with the identity as the group element. The characters, prime sets and leading-coefficient condition are not expanded.
4. There exist auxiliary data for which the twisted columns agree with the given ones and satisfy a standardness condition. The auxiliary data and the condition are not expanded.
5. A distinguished finite set $P$ of primes of $E$ equals a set specified by the base data; for every tuple two associated characters are equal. Moreover every prime in $P$ divides $g_0g_1$, and for each prime of $F$ dividing $g_0g_1$ exactly one prime in $P$ lies above it. The two characters and the set specified by the base data are not expanded.
6. For the same given realisation, there is a choice of the auxiliary data satisfying the recursive identifications in ([Compatibility of recursive coordinate realizations](https://andrewodesky.com/rh/lean/Formalism.IndefR.IndefiniteRealisation/)).

In group 1, the base-level conditions include the requirement that every tuple in the family is either the base tuple or the tuple attached to some finite place. They also include a spectral gap: at each place, two entries with different Boolean labels differ by at least $100r^4$ in absolute value, as in item 8 of ([Conditions on linked records for the period identity](https://andrewodesky.com/rh/lean/GlobalTheory.Fam.BundlePointConditions/)). The remaining base-level conditions are not expanded.
