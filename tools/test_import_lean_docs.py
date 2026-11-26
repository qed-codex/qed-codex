import unittest
from import_lean_docs import scan


class LeanNotes(unittest.TestCase):
    def test_nested_comments_strings_and_positions(self):
        source = """
def exampleText := "/-- inside a string -/"
/- ignore /-! even here -/ -/
/-! Heading -/
/-- Some /- quoted -/ content. -/
@[simp] private theorem «quoted name» : True := trivial
structure Foo where
  /-- A field -/
  x : Nat
"""
        self.assertEqual(
            scan(source)[1],
            [
                (None, " Heading "),
                ("«quoted name»", " Some /- quoted -/ content. "),
                ("Foo.x", " A field "),
            ],
        )

    def test_documented_fields_of_attributed_type_and_named_macro(self):
        source = """@[ext] structure Layer where
  /-- width -/
  width : Nat
/-- dispatch -/
macro (name := simplifyDispatch) "dispatch" : tactic => unreachable!
"""
        self.assertEqual(scan(source)[1], [("Layer.width", " width "), ("simplifyDispatch", " dispatch ")])

    def test_refuses_an_unattached_note(self):
        for source in [
            "/-- lost -/",
            "/-- lost -/\n#check Nat",
            "/-- lost -/\n/-- other -/\ndef x := 0",
            "def f := 0\n  /-- no owner -/\n  x : Nat",
        ]:
            with (
                self.subTest(source=source),
                self.assertRaisesRegex(ValueError, "unattached"),
            ):
                scan(source)

    def test_members_of_lean_types(self):
        source = """inductive T where
  /-- A constructor. -/
  | zero
structure F where
  /-- A field instance. -/
  [fin : Fintype X]
local macro "example_tactic" : tactic => `(tactic| skip)
"""
        self.assertEqual([name for name,_ in scan(source)[1]], ["T.zero", "F.fin"])

    def test_attribute_docs_and_bundled_fields(self):
        source = """/-- multiplicative -/
@[to_additive sum_eq /-- additive -/]
lemma prod_eq : True := trivial
structure Row where
  /-- carriers -/
  {A B : Type}
  /-- relation -/
  protected equal : A = B
"""
        self.assertEqual([name for name, _ in scan(source)[1]],
                         ["prod_eq", "sum_eq", "Row.A, Row.B", "Row.equal"])

    def test_local_named_syntax(self):
        self.assertEqual(
            scan("/-- syntax -/\nlocal syntax (name := sumNotation) num : term")[1],
            [("sumNotation", " syntax ")],
        )
