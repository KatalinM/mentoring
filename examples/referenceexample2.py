from examples.referenceexample import some_db
import examples.referenceexample as referenceexample

# MUTATION OF IMPORTED DATA
# When you import some_db from referenceexample, it will point to the original some_db list
print("some_db in referenceexample2 before modification:", some_db)
some_db.append(4)  # Modifying the list by appending a new value
print("some_db in referenceexample2 after modification:", some_db)
# IF WE WOULD IMPORT AGAIN, WE WOULD SEE THE MODIFIED LIST
print("This is the referenceexample.some_db after modification:", referenceexample.some_db)

some_db.clear()  # Clear the list to reset it for other tests
print("some_db in referenceexample2 after clearing:", some_db)
print("This is the referenceexample.some_db:", referenceexample.some_db)

# REASSIGNMENT OF IMPORTED VARIABLE
# If we reassign some_db to a new list, it will not affect the original some_db in referenceexample
some_db = [5, 6, 7]  # Reassigning some_db to a new list
print("some_db in referenceexample2 after reassignment:", some_db)
print("This is the referenceexample.some_db after reassignment:", referenceexample.some_db)
# The original some_db in referenceexample remains unchanged because we only modified the local reference in referenceexample2, not the original variable in referenceexample.
# From here now on, some_db in referenceexample2 points to a new list [5, 6, 7], while referenceexample.some_db still points to the original list (which is now empty after the clear() operation).

some_db.append(8)  # Modifying the new list by appending a new value
print("some_db in referenceexample2 after appending to new list:", some_db)
print("This is the referenceexample.some_db after appending to new list:", referenceexample.some_db)
