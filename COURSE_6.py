def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."
    else:

        # The variables that will be used to form the final output
        dashes=''
        space_operand_1=''
        space_operand_2=''
        space_result=''
        first_line=''
        second_line=''
        third_line=''
        fourth_line=''
        four_spaces='    '

        for problem in problems:

            operands_and_the_operator = problem.split()

            if len(operands_and_the_operator) != 3 :
                return "Error : This function supports only operand-operator-operand operations."

            operand_1 = operands_and_the_operator[0].strip()
            operand_2 = operands_and_the_operator[2].strip()
            operator = operands_and_the_operator[1].strip()

            if operator not in ["+", "-"]:
                return "Error: Operator must be '+' or '-'."
            if not (operand_1.isdigit() and operand_2.isdigit()):
                return "Error: Numbers must only contain digits."
            if len(operand_1) > 4 or len(operand_2) > 4:
                return "Error: Numbers cannot be more than four digits."

            if operator == '+':
                result = str(int(operand_1) + int(operand_2))
            else:
                result = str(int(operand_1) - int(operand_2))

            
            number_of_dashes=max(len(operand_1),len(operand_2))+2
            dashes='-'*number_of_dashes


            nr_space_operand_1 = len(dashes) - len(operand_1)
            nr_space_operand_2 = len(dashes) - len(operand_2) - 1
            nr_space_result = len(dashes) - len(result)


            space_operand_1=' '*nr_space_operand_1
            space_operand_2=' '*nr_space_operand_2
            space_result=' '*nr_space_result
            
                
            first_line += space_operand_1 + operand_1 + four_spaces
            second_line += operator + space_operand_2 + operand_2 + four_spaces
            third_line += dashes + four_spaces
            fourth_line += space_result + result + four_spaces

            output = ''
            dashes = ''
            space_operand_1 = ''
            space_operand_2 = ''
            space_result = ''
        
        if show_answers == False:
            first_line = first_line[:-4]
            second_line = second_line[:-4]
            third_line = third_line[:-4]
            final_output = first_line + '\n' + second_line + '\n' + third_line
        else:
            first_line = first_line[:-4]
            second_line = second_line[:-4]
            third_line = third_line[:-4]
            fourth_line = fourth_line[:-4]
            final_output = first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line

        return final_output

