import sys
import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--hide", choices=['count', 't_sum','t_avg','key'], nargs='+', help="Hide specified column")
parser.add_argument("--log", choices=["http", "duration", "all"], default="all", help="Log to analayse")
parser.add_argument("--sort", choices=['count', 't_sum','t_avg','key'], default='count', help="Sort criteria")
parser.add_argument("--min", type=float, default=0, help="Duration below this time will be omitted")
parser.add_argument("--type", choices=["csv", "html", "text"], default="text", help="Output type")



parser.add_argument("dir", help="Path to log dir")

args = parser.parse_args()

columns = ['count', 't_sum', 't_avg', 'key']

if not args.dir:
    args.print_help()
    sys.exit()


def sort_result(result):
    sort_index = columns.index(args.sort)
    result.sort(key=lambda mydic: mydic[args.sort])
    result.reverse()

def get_formatted_str(v):
    if type(v) == type(1):
        return str(v).rjust(8)
    elif type(v) == type(1.1):
        return '{:0.3f}'.format(v).rjust(8)
    else:
        return v

def print_table(table):
    
    print 
    
    footer = {'count':0, 't_sum':0, 't_avg':0}
    
    
    """
    if args.type == 'text':
    
        hs = '----'
    
        print '   #',
    
        for _ in columns[:-1]:
            if not is_hidden(_):
                print _.rjust(8),
                hs += ('-'*len(_)).rjust(9)
        if not is_hidden('key'):
            print '    '+table['key'],
            hs += '     '+ '-'*50
        print
        print hs
    """
    
    for ln, row in enumerate(table['rows']):
        print str(ln+1).rjust(4),

        for c in columns:
            if not is_hidden(c):
                print get_formatted_str(row[c]),

        print

def is_hidden(c):
    if args.hide and c in args.hide:
        return True

def print_result(result, k, heading):
        
    sort_result(result)



    if args.type == 'text':
    
        print heading,':'
        print '-'*(len(heading)+1)
    
        print '#'.rjust(3),
    
        for c in columns:
            if not is_hidden(c):
                
                if c=='key':
                    print '     '+k,
                else:
                    print c.rjust(8),
        print

        footer = {'count':0, 't_sum':0, 't_avg':0}

        for ln, row in enumerate(result):

                print str(ln+1).rjust(3),

                for c in columns:
                    if not is_hidden(c):
                        if c == 'key':
                            print '    ',
                        print get_formatted_str(row[c]),
                    if c in footer:
                        footer[c] += row[c]

                print

        print '='*100
        
        print ' '.rjust(3),
        for c in columns[:-1]:
            if not is_hidden(c):
                if c=='t_avg':
                    pp = footer[c] / len(result)
                else:
                    pp = footer[c]
                
                print get_formatted_str(pp),
                
        print "     GRANT TOTAL"
        print
        print

    if args.type == 'html':

        print '<table>'
        print '<caption><b>{0}</b></caption>'.format(heading)



        print '<tr><td style="padding-right:10px; padding-left:10px">#</td>',

    
        for c in columns:
            if not is_hidden(c):
                
                
                
                if c=='key':
                    td = k
                else:
                    td = c
                print '<td>{0}</td>'.format(td),
        print '</tr>'

        footer = {'count':0, 't_sum':0, 't_avg':0}

        for ln, row in enumerate(result):

                print '<tr><td align="right">{0}</td>'.format(ln+1),

                for c in columns:
                    if not is_hidden(c):
                        if c == 'key':
                            align = ''
                        else:
                            align=' align="right"'
                        print '<td {0}>{1}</td>'.format(align, get_formatted_str(row[c]).strip()),
                        
                    if c in footer:
                        footer[c] += row[c]

                print '</tr>'
        
        print '<tr><td></td>',
        for c in columns[:-1]:
            if not is_hidden(c):
                if c=='t_avg':
                    pp = footer[c] / len(result)
                else:
                    pp = footer[c]
                
                print '<td align="right">{0}</td>'.format(get_formatted_str(pp).strip()),
                
        print "<td> GRANT TOTAL </td></tr>"


        print '</table>\n'
        
        
        print '<br><br>'


def http_log():

    fn = os.path.join(args.dir, 'http_request_response.log')
    if not os.path.exists(fn):
        print "File {0} does not exists".format(fn)
        return

    rdict = {}

    for l in open(fn):
        ls = l.strip().split(' - ') 
        data = json.loads(ls[-1])
        if data.get('method') == 'GET':
            if data.get('duration'):
                d = float(data['duration'][2:-1])
                if d > args.min:
                    if data['path'] in rdict:
                        rdict[data['path']].append(d)
                    else:
                        rdict[data['path']] = [d]

    if not rdict:
        print "\n *** NO HTTP LOG ANALYSES IS AVAILABLE ***"
        return

    sn = 0
    st = 0

    result=[]

    for path in rdict:
        data = rdict[path]
        n = len(data)
        ssn = str(n).rjust(5)
        sn += n
        t = sum(data)
        st += t
        a= t/n
        
        result.append({'count': n, 't_sum': t, 't_avg': a, 'key': path})

    print_result(result, 'path', "HTTP REQUEST LOG ANALYSES")


def durations():

    fn = os.path.join(args.dir,'oxauth_persistence_duration.log')
    if not os.path.exists(fn):
        print "File {0} does not exists".format(fn)
        return

    rdict = {}

    for l in open(fn):
        ls = l.split(',')
        d = float(ls[2].strip()[12:-1])

        if d > args.min:
            if len(ls)>6:
                p = ls[5].strip()
            else:
                p = ls[4].strip()
     
            if p in rdict:
                rdict[p].append(d)
            else:
                rdict[p] = [d]

    sn = 0
    st = 0

    result = []

    for path in rdict:
        data = rdict[path]
        n = len(data)
        
        sn += n
        t = sum(data)
        a = t/n
        

        result.append({'count': n, 't_sum': t, 't_avg': a, 'key': path})

        st += t

    print_result(result, "expression", "DURATIONS LOG ANALYSES")


if args.type == 'html':
    print '<!DOCTYPE html>\n<html>\n<head>'
    print '<style>table, th, td {padding-right:10px; padding-left:10px; border: 1px solid black; border-collapse: collapse;} * {font-family: Arial, Helvetica, sans-serif;}</style>'
    print '</head>\n<body>\n'

if args.log in ('duration', 'all'):
    durations()
if args.log in ('http', 'all'):
    http_log()

if args.type == 'html':
    print '\n</body>\n</html>'
