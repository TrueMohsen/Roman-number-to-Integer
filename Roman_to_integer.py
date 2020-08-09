class RomanToInteger():
    def roman_to_integer(self,s):
            # s = s.replace('CM', '900 ').replace('M', '1000 ').replace('CD', '400 ').replace('D', '500 ').replace('XC',
            #                                                                                                      '90 ').replace(
            #     'C', '100 ').replace('XL', '40 ').replace('L', '50 ').replace('IX', '9 ').replace('X', '10 ').replace(
            #     'IV', '4 ').replace('V', '5 ').replace('I', '1 ')
            # s = s.split()
            # sum = 0
            # for _ in s:
            #     sum += int(_)
            # return (sum)
            result = 0
            o_roman=roman
            if len(o_roman)==0:
                return 0
            elif len(o_roman) == 1:
                if o_roman=='I':
                    return 1
                elif o_roman=='V':
                    return 5
                elif o_roman=='X':
                    return 10
                elif o_roman=='L':
                    return 50
                elif o_roman=='C':
                    return 100
                elif o_roman=='D':
                    return 500
                elif o_roman=='M':
                    return 1000


            if 'M' in o_roman:
                o_roman.index('M')
                result=result+1000
                sub=self.roman_to_integer(o_roman[0:o_roman.index('M')])
                add=self.roman_to_integer(o_roman[o_roman.index('M')+1:])
                result = result+add-sub
                return result
            elif 'D' in o_roman:
                result = result + 500
                o_roman.index('D')
                sub = self.roman_to_integer(o_roman[0:o_roman.index('D')])
                add = self.roman_to_integer(o_roman[o_roman.index('D')+1:])
                result = result + add - sub
                return result
            elif 'C' in o_roman:
                result = result + 100
                o_roman.index('C')
                sub = self.roman_to_integer(o_roman[0:o_roman.index('C')])
                add = self.roman_to_integer(o_roman[o_roman.index('C')+1:])
                result = result + add - sub
                return result

            elif 'L' in o_roman:
                result = result + 50
                o_roman.index('L')
                sub = self.roman_to_integer(o_roman[0:o_roman.index('L')])
                add = self.roman_to_integer(o_roman[o_roman.index('L')+1:])
                result = result + add - sub
                return result

            elif 'X' in o_roman:
                result = result + 10
                o_roman.index('X')
                sub = self.roman_to_integer(o_roman[0:o_roman.index('X')])
                add = self.roman_to_integer(o_roman[o_roman.index('X')+1:])
                result = result + add - sub
                return result

            elif 'V' in o_roman:
                result = result + 5
                o_roman.index('V')
                sub = self.roman_to_integer(o_roman[0:o_roman.index('V')])
                add = self.roman_to_integer(o_roman[o_roman.index('V')+1:])
                result = result + add - sub
                return result

            elif 'I' in o_roman:
                result = result + 1
                o_roman.index('I')
                sub = self.roman_to_integer(o_roman[0:o_roman.index('I')])
                add = self.roman_to_integer(o_roman[o_roman.index('I')+1:])
                result = result + add - sub
                return result

            return result


if __name__=='__main__' :
    cs = RomanToInteger()
    result=cs.roman_to_integer('MMXXIV')
    print('result is '+str(result))

