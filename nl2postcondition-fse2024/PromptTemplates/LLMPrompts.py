from string import Template

#################################################################
# HUMANEVAL TEMPLATES
#################################################################

systemMessage="You are a programming assistant that generates executable python only. You generate correct code, so you only generate code you are sure of. You have Python comments explaining your intent when possible."


#################################################################
#Template for BASE PROMPT, NO REFERENCE
#################################################################

genOneNoRef=Template("""You have the following Python code, including a function stub and docstring for ${entrypoint}:

${codeStubAndDocstring}

Please write exactly one ${toGenerateFull} that can be used to increase confidence that ${entrypoint} is implemented correctly according to the specification in its docstring${promptAdds}. Please write the ${toGenerateShort} in Python, and use exactly one python assert statement at the end of the ${toGenerateShort}. Include a Python comment before the ${toGenerateShort} explaining what the ${toGenerateShort} ${toGenerateGoal}.  ${toUse}. Do not return any other textual description of the code other than the Python comment.

Specifically, the format of your response should be:

```
# Comment explaining what the ${toGenerateShort} does
CODE FOR EXACTLY ONE ${toGenerateShortCaps} USING ASSERT GOES HERE
```
""")

#################################################################
#Template for SIMPLE PROMPT, NO REFERENCE
#################################################################

genOneNoRef_simple=Template("""You are provided with the following Python function stub and docstring for ${entrypoint}. You want to ensure that when the function is implemented, it complies with the specification given in the docstring:

${codeStubAndDocstring}

Your task is to write a ${toGenerateFull} for ${entrypoint}. The ${toGenerateShort} should be in Python and consist of exactly one assert statement. A Python comment explaining the ${toGenerateShort}'s meaning should precede it. For variables, the ${toGenerateShort} should only use the input parameters defined in the function stub and a hypothetical return value of the function, which we'll assume is stored in a variable `return_value`.

For string manipulation, Python's re (regular expressions) library can be used. If other Python standard library functions are necessary, include the corresponding imports. However, refrain from using external libraries or calling the function itself (in this case, ${entrypoint}) within the ${toGenerateShort}.

If the ${toGenerateShort} calls any functions, they should only be those from the functional subset of Python. By this, we mean functions that are pure (i.e., no side effects, depends only on input values) such as `all()`, `len()`, `map()`, `filter()`, etc.

Although the ${toGenerateShort} should be less computationally complex than the function itself and relatively simple, it should not be trivial. It should encapsulate an aspect of the function output specification without implementing the function itself and should be easily readable by a human.

While not trivial, your ${toGenerateShort} should still be very simple and short. It should be a single line of code that is not too long, and it should capture only one aspect of the function's behavior, not all of it. For example, if the goal of the function were to sort a list, you might write a ${toGenerateShort} that checks that the elements in the list are in sorted order, or you might write a ${toGenerateShort} that checks that the list is the same length as the input list. You would not write a ${toGenerateShort} that checks both of these things.

The format of your response should be:
```
# Comment explaining what aspect of the function the ${toGenerateFull} checks
CODE FOR EXACTLY ONE ${toGenerateShortCaps} USING ASSERT GOES HERE
``` 

The ${toGenerateShort} should hold true whenever the function ${entrypoint} executes successfully as specified in the docstring, regardless of the eventual internal implementation of the function.     
""")

#################################################################
#Postcondition specific subprompts
#################################################################

postCondToUse = Template("For variables, only use the function inputs and the return value of the function. You can use python's re (regular expressions) if needed to deal with strings. Do not call ${entrypoint} itself in the postcondition. Instead, assume that the function has already been called and its return value is available in a variable called `return_value` that you can use. In the postcondition, only use functions that are part of the functional subset of python (e.g., all(), len(), map(), filter(), etc.)")

#################################################################
#Template for BASE, With reference solution in prompt
#################################################################


# Template for generating a post condition given the reference solution 
genOneWithRef = Template("""You have the following Python code${promptAdds}, including the function ${entrypoint} that behaves as specified in its docstring:

${codeStubAndDocstring}

Please write exactly one ${toGenerateFull} for ${entrypoint}. Please write the ${toGenerateShort} in Python, and use exactly one python assert statement at the end of the ${toGenerateShort}. Include a Python comment before the ${toGenerateShort} explaining what the ${toGenerateShort} ${toGenerateGoal}.  ${toUse}. Do not return any other textual description of the code other than the Python comment.

Specifically, the format of your response should be:

```
# Comment explaining what the ${toGenerateShort} does
CODE FOR EXACTLY ONE ${toGenerateShortCaps} USING ASSERT GOES HERE
```
""")

#################################################################
#Template for SIMPLE, With reference solution in prompt
#################################################################

genOneWithRef_simple=Template("""You are provided with the following Python function implementation for ${entrypoint}, and you want to ensure it is implemented correctly according to the specification in the docstring:

${codeStubAndDocstring}

Your task is to write a ${toGenerateFull} for ${entrypoint}. The ${toGenerateShort} should be in Python, and consist of exactly one assert statement. A Python comment explaining the ${toGenerateShort}'s meaning should precede it. For variables, the ${toGenerateShort} should only use the input parameters defined in the function stub and a hypothetical return value of the function, which we'll assume is stored in a variable `return_value`.

For string manipulation, Python's `re` (regular expressions) library can be used. If other Python standard library functions are required, include the necessary imports. However, refrain from using external libraries or calling the function itself (in this case, ${entrypoint}) within the ${toGenerateShort}.

If the ${toGenerateShort} calls any functions, they should only be those from the functional subset of Python. By this, we mean functions that are pure (i.e., no side effects, depends only on input values) such as `all()`, `len()`, `map()`, `filter()`, etc.

Although the ${toGenerateShort} should be less computationally complex than the function itself and relatively simple, it should not be trivial. It should encapsulate an aspect of the function output specification without implementing the function itself and should be easily readable by a human.

While not trivial, your ${toGenerateShort} should still be very simple and short. It should be a single line of code that is not too long, and it should capture only one aspect of the function's behavior, not all of it. For example, if the goal of the function were to sort a list, you might write a ${toGenerateShort} that checks that the elements in the list are in sorted order, or you might write a ${toGenerateShort} that checks that the list is the same length as the input list. You would not write a ${toGenerateShort} that checks both of these things.

The format of your response should be:
```
# Comment explaining what aspect of the function the ${toGenerateFull} checks
CODE FOR EXACTLY ONE ${toGenerateShortCaps} USING ASSERT GOES HERE
``` 

The ${toGenerateShort} should hold true whenever the function ${entrypoint} executes successfully as specified in the docstring, regardless of its internal implementation.        
""")


#################################################################
#Templates for generating code solutions
#################################################################

# Template for generating code
genCode=Template("""Given the code below, please implement the body of the function ${entrypoint} such that it behaves as described in the given docstring. 

${codeStubAndDocstring}

Return only the starter code and the function implementation. Do not return any other textual description or comments. Specifically, the format of your response should be:

```python
${codeStubAndDocstring}
    # Your implementation goes here
```
""")

genCodeBuggy=Template("""Given the code below, please implement the body of the function ${entrypoint}. It should behave mostly as expected in the docstring, but please insert at least one bug into your implementation of ${entrypoint}. The bug should be minor enough that your implementation will fail some test cases, but not all.

${codeStubAndDocstring}

Return only the starter code and the buggy function implementation. Do not return any other textual description or comments. Specifically, the format of your response should be:

```python
${codeStubAndDocstring}
    # Your implementation goes here
```
""")

#################################################################
# DEFECTS4J TEMPLATES
#################################################################


systemMessage="You are a programming assistant that generates executable java only. You generate correct code, so you only generate code you are sure of. You have java comments explaining your intent when possible."


#################################################################
#Template for ONE GENERATED, NO REFERENCE GIVEN
#################################################################

# Template for generating postcondition without the reference code
genOneNoRef=[
Template("""You have some java code which includes the method stub for the unimplemented method `${entrypointLong}`. This code may contain a natural language comment or Javadoc before ${entrypoint} specifying the correct behavior of the method. You want to ensure that when the method is implemented, it behaves as specified in the Javadoc:

${codeStubAndDocstring}

Your task is to write a ${toGenerateFull} for ${entrypoint}. The ${toGenerateShort} should be in Java and consist of exactly one `assert` statement. A Java comment explaining the ${toGenerateShort}'s meaning should precede it. For variables, the ${toGenerateShort} should only use the input parameters defined in the method stub${postCondExtra1}.

If the ${toGenerateShort} requires any Java standard library functions, include the corresponding imports. However, refrain from using external libraries or calling the method itself (in this case, ${entrypoint}) within the ${toGenerateShort}.

If the ${toGenerateShort} calls any methods, they should only be those from the functional subset of Java. By this, we mean methods that are pure (i.e., no side effects, depends only on input values).

${postCondExtra2}

The format of your response should be:
```
// Comment explaining what aspect of the method the ${toGenerateFull} checks
CODE FOR EXACTLY ONE ${toGenerateShortCaps} USING ASSERT GOES HERE
``` 

The ${toGenerateShort} should hold true whenever the method ${entrypoint} executes successfully as specified in the Javadoc, regardless of the eventual internal implementation of the method.
""")]

#################################################################
#Template for ONE GENERATED, REFERENCE GIVEN
#################################################################

genOneWithRef=[
Template("""You have some java code which includes the method `${entrypointLong}`. This code may contain a natural language comment or Javadoc before ${entrypoint} specifying its correct behavior. You want to ensure that when the method is implemented, it behaves as specified in the Javadoc:

${codeStubAndDocstring}

Your task is to write a ${toGenerateFull} for ${entrypoint}. The ${toGenerateShort} should be in Java and consist of exactly one `assert` statement. A Java comment explaining the ${toGenerateShort}'s meaning should precede it. For variables, the ${toGenerateShort} should only use the input parameters defined in the method stub${postCondExtra1}.

If the ${toGenerateShort} requires any Java standard library functions, include the corresponding imports. However, refrain from using external libraries or calling the method itself (in this case, ${entrypoint}) within the ${toGenerateShort}.

If the ${toGenerateShort} calls any methods, they should only be those from the functional subset of Java. By this, we mean methods that are pure (i.e., no side effects, depends only on input values).

${postCondExtra2}

The format of your response should be:
```
// Comment explaining what aspect of the method the ${toGenerateFull} checks
CODE FOR EXACTLY ONE ${toGenerateShortCaps} USING ASSERT GOES HERE
``` 

Should they conflict, the ${toGenerateShort} should hold true whenever the method ${entrypoint} executes successfully as specified in the Javadoc, regardless of the actual implementation of the method.
""")]


#################################################################
#Postcondition specific subprompts
#################################################################
postCondExtra1 = """ and a hypothetical return value of the method, which we'll assume is stored in a variable `returnValue`"""

postCondExtra2 = """Although the postcondition should be less computationally complex than the method itself and relatively simple, it should not be trivial. It should encapsulate an aspect of the method output specification without implementing the method itself and should be easily readable by a human.

While not trivial, your postcondition should still be very simple and short. It should be a single line of code that is not too long, and it should capture only one aspect of the method's behavior, not all of it. For example, if the goal of the method were to sort a list, you might write a postcondition that checks that the elements in the list are in sorted order, or you might write a postcondition that checks that the list is the same size as the input list. You would not write a postcondition that checks both of these things."""
