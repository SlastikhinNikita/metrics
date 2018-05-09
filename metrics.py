import psutil
import argparse


class TextColor:
    HEADER      = '\033[95m'
    BLUE        = '\033[94m'
    GREEN       = '\033[92m'
    YELLOW     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'
    WHITE       = '\033[0m'
    RED         = '\033[31m'
    PURPLE      = '\033[35m'
    CYAN        = '\033[36m'


def printMemInfo():
    """
        Main function
    """
    total, available, percent, used, free, active, inactive, buffers, cached, shared, slab = psutil.virtual_memory()
    print("virtual total \t",TextColor.GREEN,total,TextColor.WHITE)
    print("virtual used \t",TextColor.GREEN,used,TextColor.WHITE)
    print("virtual free \t",TextColor.GREEN,free,TextColor.WHITE)
    print("virtual shared \t",TextColor.GREEN,shared,TextColor.WHITE)
    total, used, free, percent, sin, sout = psutil.swap_memory()
    print("swap total \t",TextColor.GREEN,total,TextColor.WHITE)
    print("swap used \t",TextColor.GREEN,used,TextColor.WHITE)
    print("swap free \t",TextColor.GREEN,free,TextColor.WHITE)	



def printCPUInfo(percpu):
    """
        Main function
    """
    if percpu == '1':
        i = 0
        for a in psutil.cpu_times(True):
            user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice = a 
            print("{}CPU unit[{}]{}".format(TextColor.YELLOW,i,TextColor.WHITE))
            print("system.cpu.idle \t",TextColor.GREEN,idle,TextColor.WHITE)
            print("system.cpu.user \t",TextColor.GREEN,user,TextColor.WHITE)
            print("system.cpu.guest \t",TextColor.GREEN,guest,TextColor.WHITE)
            print("system.cpu.iowait \t",TextColor.GREEN,iowait,TextColor.WHITE)
            print("system.cpu.system \t",TextColor.GREEN,system,TextColor.WHITE)
            print("system.cpu.stolen \t",TextColor.GREEN,steal,TextColor.WHITE)
            i = i + 1
    else:		
        user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice = psutil.cpu_times()
        print("system.cpu.idle \t",TextColor.GREEN,idle,TextColor.WHITE)
        print("system.cpu.user \t",TextColor.GREEN,user,TextColor.WHITE)
        print("system.cpu.guest \t",TextColor.GREEN,guest,TextColor.WHITE)
        print("system.cpu.iowait \t",TextColor.GREEN,iowait,TextColor.WHITE)
        print("system.cpu.system \t",TextColor.GREEN,system,TextColor.WHITE)
        print("system.cpu.stolen \t",TextColor.GREEN,steal,TextColor.WHITE)	
			



def main():
    """
        Main function
    """
    parser = argparse.ArgumentParser(description='Use param: mem or cpu. For non-one core cpu you can use param --percpu')
    parser.add_argument('param', metavar='PARAM',
                    help='parameter of output')
    parser.add_argument('-p','--percpu', action='store_const', const='1', help='for non-one core cpu output', default='False')

    args = vars(parser.parse_args())	
	
    if args['param'] == 'mem':
        printMemInfo()
		
    if args['param'] == 'cpu':
        printCPUInfo(parser.parse_args().percpu)	


if __name__ == '__main__':
    main()	