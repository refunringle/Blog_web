import argparse
from ast import arg
from distutils.log import error
import logging
from flask import Flask, request

#import create_db as dbs
from app import db

logger = None

def parse_args():
    parser = argparse.ArgumentParser(description = "Web crawler")
    parser.add_argument("-d", "--debug", help = "Enable debug logging", action="store_true")
    parser.add_argument("--db", help="Name of database to use", action="store", default="blog")
    subcommands = parser.add_subparsers(help="Commands", dest="command", required=True)
    subcommands.add_parser("cdb", help="creating our database")
    subcommands.add_parser("ctb", help="creating tables in database")

    return parser.parse_args()

def configure_logging(level=logging.INFO):
    global logger
    logger = logging.getLogger("blog_web")
    logger.setLevel(level)
    screen_handler = logging.StreamHandler()
    screen_handler.setLevel(level)
    formatter = logging.Formatter("[%(levelname)s] : %(filename)s(%(lineno)d) : %(message)s")
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)



# def create_tables(db_name):
#     conn = db.get_connection(db_name)
#     with conn.cursor() as cursor:
#         with open("init.sql") as f:
#             sql = f.read()
#             cursor.execute(sql)
#     conn.commit()
#     conn.close()

# def insert_data_to_database(url):
#     for artist_name, artist_url in artist(url).items():
#         artist_id = db.add_artist(artist_name)
#         for songs, song_url in get_songs_list(artist_url).items():
#             lyrics = song_lyrics(song_url)
#             db.add_song(songs, artist_id, lyrics)
            
def do_admin_login():
   POST_USERNAME = str(request.form['username'])
   POST_PASSWORD = str(request.form['password'])

   Session = db.sessionmaker(bind=db.engine)
   s = Session()
   query = s.query(db.users).filter(db.users.email.in_([POST_USERNAME]),
                                    db.users.password.in_([POST_PASSWORD]) )
   result = query.first()
   if result:
       db.session['logged_in'] = True
   else:
       error('wrong password!')
#return home()



def main():
    args = parse_args()

    if args.debug:
        configure_logging(logging.DEBUG)
    else:
        configure_logging(logging.INFO)
    
    # if args.command =="cdb":
    #     logger.info("Creating Database")
    #     create_tables(args.db)
        
    if args.command =="ctb":
        logger.info("Creating Database")
        db.create_all()
        # insert_data_to_database(url_address)
    else:
        logger.warning("%s not implemented", args.command)

if __name__ == "__main__":
    main()